from django.shortcuts import render, redirect
from .models import Item
from .forms import CreateItemForm
from django.contrib import messages

# Create your views here.

def create(request):
    context = {}
    if request.user.is_staff:
        if request.method == 'POST':
            form = CreateItemForm(request.POST)
            if form.is_valid():
                form.save()
                title = form.cleaned_data.get('title')
                messages.success(request, f'Item {title} created successfully!')
                return redirect('dashboard')
        else:
            form = CreateItemForm()
    else:
        messages.warning(request, f'Not an Admin')
        return redirect('dashboard')

    context['form'] = form
    return render(request=request, template_name='inventory/create-item.html', context= context)

            


    