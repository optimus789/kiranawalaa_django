from django.contrib import auth
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf.urls import url
from .views import ChartData
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('dashboard/cust/create/', user_views.createcust, name='cust-create'),
    path("dashboard/cust/update/<int:pk>", user_views.custupdate, name="cust-update"),
    path('dashboard/cust/delete/<int:pk>', user_views.deletecust, name='cust-delete'),
    path('dashboard/cust/', user_views.custlist, name='cust'),
    path("dashboard/delv/update/<int:pk>", user_views.delvryupdate, name="delv-update"),
    path('dashboard/delv/create/', user_views.createdelvry, name='delv-create'),
    path('dashboard/delv/delete/<int:pk>', user_views.deletedelv, name='delv-delete'),
    path('dashboard/delv/', user_views.delvrylist, name='delv'),
    url(r"^api/chart/data/$",ChartData.as_view()),
]