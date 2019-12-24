from django.contrib import auth
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from . import views


urlpatterns = [
    path('', views.inventorylist, name='inventory'),
    path('create/', views.create, name='create-item'),
    path("item/<int:pk>", views.update, name="post-update")
]