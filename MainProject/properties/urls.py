from django.urls import path
from .views import *

urlpatterns = [
    path('properties/', property_list, name='property_list'),

    path('property/<int:pk>/', property_detail, name='property_detail'),
    path('properties/<int:id>/book/', book_visit, name='book_visit'),

    # Agent routes:
  
    path('agent/add/', add_property, name='add_property'),
    path('dashboard/', agent_dashboard, name='agent_dashboard'),
    path('edit/<int:property_id>/', edit_property, name='edit_property'),
    path('delete/<int:property_id>/', delete_property, name='delete_property'),
    path('chat/<int:property_id>/<int:agent_id>/', chat_view, name='chat'),
    path('inbox/', inbox, name='inbox'),
]
