from django.urls import path


from .views import home_view, login_view, register_view, logout_view, user_dashboard

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login_user'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout_user'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
]

