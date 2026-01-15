from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from properties.models import Property
from .models import VisitRequest

@login_required
def book_visit(request, id):
    property_obj = get_object_or_404(Property, id=id)

    # Prevent duplicate booking
    existing = VisitRequest.objects.filter(
        user=request.user,
        property=property_obj
    ).first()

    if existing:
        messages.warning(request, "You have already requested a visit for this property.")
        return redirect('property_detail', id=id)

    VisitRequest.objects.create(
        user=request.user,
        property=property_obj
    )

    messages.success(request, "Visit request submitted successfully! We will contact you soon.")
    return redirect('property_detail', id=id)


def visit_success(request):
    return render(request, "visits/success.html")
