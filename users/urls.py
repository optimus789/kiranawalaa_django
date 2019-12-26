from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='home'),
    path("register/", user_views.register, name="register"),
    path("/logout", views.logout_view, name="logout")
]