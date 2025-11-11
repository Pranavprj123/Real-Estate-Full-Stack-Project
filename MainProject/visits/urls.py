from django.urls import path
from .views import visit_success

urlpatterns = [
    path('success/', visit_success, name='visit_success'),
]
