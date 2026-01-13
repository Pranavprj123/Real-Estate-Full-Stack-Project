from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from visits.models import VisitRequest
from django.contrib.auth.decorators import login_required
from accounts.decorators import agent_required
from .forms import PropertyForm, PropertyImageForm
from django.contrib.auth.models import User
from .models import Property, PropertyImage, Wishlist
from django.contrib import messages
from django.db.models import Q
from .models import Wishlist

# Create your views here.


def property_list(request):
    properties = Property.objects.all()

    city = request.GET.get("city")
    bhk = request.GET.get("bhk")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    if city:
        properties = properties.filter(city__icontains=city)

    if bhk:
        properties = properties.filter(bhk=bhk)

    if min_price:
        properties = properties.filter(price__gte=min_price)

    if max_price:
        properties = properties.filter(price__lte=max_price)

    return render(request, "property_list.html", {"properties": properties})


def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    context = {"property": property}
    return render(request, "properties/property_detail.html", context)

def listings_view(request):
    properties = Property.objects.all()
    return render(request, "properties/listings.html", {"properties": properties})

@login_required
def add_to_wishlist(request, pk):
    property_obj = Property.objects.get(id=pk)

    Wishlist.objects.get_or_create(
        user=request.user,
        property=property_obj
    )

    messages.success(request, "Added to wishlist!")
    return redirect('property_detail', pk=pk)

def book_visit(request, id):
    property = get_object_or_404(Property, id=id)

    # Auto assign today's date or next day (your choice)
    visit_date = date.today()

    VisitRequest.objects.create(
        property=property,
        user=request.user,
        visit_date=visit_date,
        status="approved"   # ✅ No approval required
    )

    return redirect("visit_success")

@login_required
@agent_required
def agent_dashboard(request):
    my_properties = Property.objects.filter(owner=request.user)
    return render(request, "agent/agent_dashboard.html", {"properties": my_properties})


@login_required
@agent_required
def add_property(request):
    # ⛔ Block if agent is not verified
    if not hasattr(request.user, 'agentprofile') or not request.user.agentprofile.is_agent_verified:
        messages.warning(request, "You are not verified to list properties. Please wait for admin approval.")
        return redirect('home')  # Change 'home' if your homepage URL name is different.

    if request.method == 'POST':
        form = PropertyForm(request.POST)
        images = request.FILES.getlist('image')

        if form.is_valid():
            property_obj = form.save(commit=False)
            # assign logged in user to the appropriate field (owner or agent)
            if hasattr(property_obj, 'owner'):
                property_obj.owner = request.user
            else:
                property_obj.agent = request.user
            property_obj.save()

            for img in images:
                PropertyImage.objects.create(property=property_obj, image=img)

            messages.success(request, "Property added successfully!")
            return redirect('property_list')

    else:
        form = PropertyForm()
        image_form = PropertyImageForm()

    return render(request, 'properties/add_property.html', {'form': form, 'image_form': image_form})

def agent_dashboard(request):
    # Only show properties of logged-in agent
    properties = Property.objects.filter(agent=request.user)
    return render(request, 'properties/agent_dashboard.html', {'properties': properties})


def edit_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id, agent=request.user)

    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Property updated successfully!")
            return redirect('agent_dashboard')
    else:
        form = PropertyForm(instance=property_obj)

    return render(request, 'properties/edit_property.html', {'form': form})

def delete_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id, agent=request.user)
    property_obj.delete()
    messages.success(request, "Property deleted successfully!")
    return redirect('agent_dashboard')


# def chat_view(request, property_id, agent_id):
#     property_obj = Property.objects.get(id=property_id)
#     agent = User.objects.get(id=agent_id)

#     if request.user == agent:
#         receiver = None  # agent will reply to selected buyer later
#     else:
#         receiver = agent  # buyer sends to agent

#     # Fetch chat messages between these two
#     messages_qs = ChatMessage.objects.filter(
#         property=property_obj,
#         sender__in=[request.user, agent],
#         receiver__in=[request.user, agent]
#     )

#     if request.method == "POST":
#         form = ChatMessageForm(request.POST)
#         if form.is_valid():
#             msg = form.save(commit=False)
#             msg.sender = request.user
#             msg.receiver = agent if request.user != agent else request.POST.get("receiver")
#             msg.property = property_obj
#             msg.save()
#             return redirect('chat', property_id=property_id, agent_id=agent_id)

#     else:
#         form = ChatMessageForm()

#     return render(request, 'properties/chat.html', {
#         'form': form,
#         'messages': messages_qs,
#         'property': property_obj,
#         'agent': agent
#     })

def get_unread_count(user):
    return ChatMessage.objects.filter(receiver=user, is_read=False).count()

def inbox(request):
    chats = ChatMessage.objects.filter(receiver=request.user).order_by('-timestamp')
    
    # mark as read when inbox opened
    ChatMessage.objects.filter(receiver=request.user, is_read=False).update(is_read=True)

    return render(request, 'properties/inbox.html', {'chats': chats})
    