from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Deliveryguy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, CustomerCreateForm, DelvrygyFormCreate


def home(request):
    return render(request, 'users/index.html')


def register(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('dashboard')
        else:
            form = UserRegisterForm()
    else:
        messages.warning(request, f'Not an admin')
        return redirect('dashboard')

    return render(request, 'dashboard/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, f'You have successfully Logged out')
    return redirect('login')


def custlist(request):
    if request.user.is_staff:
        context = {"custs": Customer.objects.all()}
        return render(request, 'users/cust.html', context)
    else:
        messages.warning(request, f'Not an Admin')
        return redirect('/')
    

def createcust(request):
    context = {}
    if request.user.is_staff:
        if request.method == 'POST':
            form = CustomerCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                name = form.cleaned_data.get('name')
                messages.success(request, f'Customer {name} created successfully!')
                context['form'] = form
                return render(request=request, template_name='users/create-cust.html', context=context)
        else:
            form = CustomerCreateForm()
            context['form'] = form
            return render(request=request, template_name='users/create-cust.html', context=context)
    else:
        messages.warning(request, f'Not an Admin')
        return redirect('/')




