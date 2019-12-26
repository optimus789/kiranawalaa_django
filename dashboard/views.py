from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='/login') 
def dashboard(request):
    if request.user.is_staff:
        return render(request, 'dashboard/admin.html')
    else:
        messages.warning(request, f'Not an admin')
        return redirect('/')


