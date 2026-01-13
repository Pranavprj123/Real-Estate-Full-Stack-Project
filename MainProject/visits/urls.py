from django.urls import path

from . import views
from .views import visit_success, book_visit    

urlpatterns = [
    path('success/', visit_success, name='visit_success'),
    path('book/<int:id>/', views.book_visit, name='book_visit'),
]
