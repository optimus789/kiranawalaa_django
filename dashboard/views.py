from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Customer, Deliveryguy

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from inventory.models import Orders

@login_required(login_url='/login') 
def dashboard(request):
    if request.user.is_staff:
        instance = get_object_or_404(User, id=request.user.id)
        
        context = {
            'users':instance,
            'custs': Customer.objects.all(),
            'orders': Orders.objects.all(),
            'dagents': Deliveryguy.objects.all(),
            'count' :  Orders.objects.filter(status="In Process").count()
        }
        return render(request, 'dashboard/admin.html', context)
    else:
        messages.warning(request, f'Not an admin')
        return redirect('/')


