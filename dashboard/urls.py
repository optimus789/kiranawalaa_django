from django.contrib import auth
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ='dashboard/logout.html'), name='logout'),
]