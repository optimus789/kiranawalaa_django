from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from .forms import UserRegisterForm


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




