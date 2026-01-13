from django.urls import path
from .views import listings_view, property_list, property_detail, add_property, add_to_wishlist

urlpatterns = [
    path('', property_list, name='property_list'),
    path("listings/", listings_view, name="listings"),
    path('<int:pk>/', property_detail, name='property_detail'),
    path('<int:pk>/wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('add/', add_property, name='add_property'),
]
