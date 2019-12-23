from django.contrib import auth
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', include('users.urls')),
]