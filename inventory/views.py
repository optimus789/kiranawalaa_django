from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemCreateForm, ItemUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.views.generic import UpdateView

# Create your views here.
@login_required(login_url='/login')
def inventorylist(request):
    if request.user.is_staff:
        context = {"items": Item.objects.all()}
        return render(request, 'inventory/inventory.html', context)
    else:
        messages.warning(request, f'Not an Admin')
        return redirect('/')
    

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
                context['form'] = form
                return render(request=request, template_name='inventory/create-item.html', context=context)
        else:
            form = ItemCreateForm()
            context['form'] = form
            return render(request=request, template_name='inventory/create-item.html', context=context)
    else:
        messages.warning(request, f'Not an Admin')
        return redirect('/')


def update(request, pk):
    """if request.method == 'POST':
        title = request.POST.get("title")
        desc = request.POST.get("desc")           
        category = request.POST.get("category")           
        mail = request.POST.get("mail")
        Item.objects.filter(id=pk).update(name="Downtown (Madison)")"""
    if request.user.is_staff:
        instance1 = get_object_or_404(Item, id=pk)
        u_form = ItemUpdateForm(request.POST, request.FILES, instance=instance1)
        if u_form.is_valid():
            title = u_form.cleaned_data.get('title')
            """desc = u_form.cleaned_data.get('desc')
            category = u_form.cleaned_data.get('category')
            cprice = u_form.cleaned_data.get('cprice')
            sprice = u_form.cleaned_data.get('sprice')
            mrp = u_form.cleaned_data.get('mrp')
            tax = u_form.cleaned_data.get('tax')
            units = u_form.cleaned_data.get('units')
            image = u_form.cleaned_data.get('image')
            stock = u_form.cleaned_data.get('stock')"""
            u_form.save()
            messages.success(request, f'Item {title} has been updated successfully')
            return redirect('inventory')

        context = {
        'u_form': u_form,
        'item':instance1
        }

        return render(request, 'inventory/item-update.html', context)
    else:
        messages.warning(request, f'Not an Admin')
        return redirect('/')
        

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


            


    