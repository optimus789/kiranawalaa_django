from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='/login') 
def dashboard(request):
    if request.user.is_staff:
        instance = get_object_or_404(User, id=request.user.id)
        context = {
            'users':instance
        }
        return render(request, 'dashboard/admin.html', context)
    else:
        messages.warning(request, f'Not an admin')
        return redirect('/')


