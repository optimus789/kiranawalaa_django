from django.shortcuts import render
from .models import Item

# Create your views here.

def create(request):
    return render(
                  request = request,
                  template_name='inventory/create-item.html',
                  context={'item':Item.objects})