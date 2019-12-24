from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemCreateForm, ItemUpdateForm
from django.contrib import messages
from django.views.generic import UpdateView

# Create your views here.

def inventorylist(request):
    context = {"items": Item.objects.all()}
    return render(request, 'inventory/inventory.html', context)

def create(request):
    context = {}
    if request.user.is_staff:
        if request.method == 'POST':
            form = ItemCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                title = form.cleaned_data.get('title')
                messages.success(request, f'Item {title} created successfully!')
                return redirect('inventory')
        else:
            form = ItemCreateForm()
    else:
        messages.warning(request, f'Not an Admin')
        return redirect('dashboard')

    context['form'] = form
    return render(request=request, template_name='inventory/create-item.html', context=context)


def update(request, pk):
    instance = get_object_or_404(Item, id=pk)
    u_form = ItemUpdateForm(request.POST, request.FILES)
    if u_form.is_valid():
        u_form.save()
        title = u_form.cleaned_data.get('title')
        messages.success(request, f'Item {title} has been updated successfully')
        return redirect('inventory')

    context = {
    'u_form': u_form
    }

    return render(request, 'inventory/item-update.html', context)
        

"""class ItemUpdateView(UpdateView):
    model = Item
    fields = ['title', 'desc', 'category', 'image', 'cprice', 'sprice', 'mrp', 'tax', 'stock', 'units']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    """


            


    