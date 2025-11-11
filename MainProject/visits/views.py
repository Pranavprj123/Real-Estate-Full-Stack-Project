from django.shortcuts import render

# Create your views here.

def visit_success(request):
    return render(request, "visits/success.html")
