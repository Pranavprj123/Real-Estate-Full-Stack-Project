from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from properties.models import Property
from visits.models import VisitRequest
from django.contrib.auth.decorators import login_required   


# ========================= HOME PAGE =========================
def home_view(request):
    properties = Property.objects.all()
    return render(request, 'home.html', {
        'properties': properties
    })


# ========================= LOGIN =========================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


# ========================= REGISTER =========================
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Password match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Email exists check
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('register')

        # Username exists check
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return redirect('register')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'accounts/register.html')


# ========================= LOGOUT =========================
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login_user')

@login_required
def user_dashboard(request):
    visits = VisitRequest.objects.filter(
        user=request.user
    ).select_related('property').order_by('-created_at')

    # Show notifications based on latest visit status
    latest = visits.first()
    if latest:
        if latest.status == 'approved':
            messages.success(
                request,
                f"Your visit request for '{latest.property.title}' has been approved!"
            )
        elif latest.status == 'rejected':
            messages.error(
                request,
                f"Your visit request for '{latest.property.title}' was rejected."
            )

    return render(request, 'dashboard.html', {
        'visits': visits
    })
