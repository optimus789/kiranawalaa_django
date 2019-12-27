from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.db.models import F
from .forms import ItemCreateForm, ItemUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.views.generic import UpdateView

# Create your views here.
@login_required(login_url="/login")
def inventorylist(request):
    if request.user.is_staff:
        context = {"items": Item.objects.all()}
        return render(request, "inventory/inventory.html", context)
    else:
        messages.warning(request, f"Not an Admin")
        return redirect("/")


def create(request):
    context = {}
    if request.user.is_staff:
        if request.method == "POST":
            form = ItemCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                title = form.cleaned_data.get("title")
                messages.success(request, f"Item {title} created successfully!")
                return redirect("inventory")
                context["form"] = form
                return render(
                    request=request,
                    template_name="inventory/create-item.html",
                    context=context,
                )
        else:
            form = ItemCreateForm()
            context["form"] = form
            return render(
                request=request,
                template_name="inventory/create-item.html",
                context=context,
            )
    else:
        messages.warning(request, f"Not an Admin")
        return redirect("/")


def update(request, pk):

    if request.user.is_staff:
        instance1 = get_object_or_404(Item, id=pk)
        u_form = ItemUpdateForm(request.POST, request.FILES, instance=instance1)
        if request.method == "POST":
            title1 = request.POST.get("title")
            desc1 = request.POST.get("desc")
            category1 = request.POST.get("category")
            cprice1 = request.POST.get("cprice")
            sprice1 = request.POST.get("sprice")
            mrp1 = request.POST.get("mrp")
            tax1 = request.POST.get("tax")
            stock1 = request.POST.get("stock")
            units1 = request.POST.get("units")
            img = request.FILES.get("image")
            Item.objects.filter(id=pk).update(title=title1)
            Item.objects.filter(id=pk).update(desc=desc1)
            Item.objects.filter(id=pk).update(category=category1)
            Item.objects.filter(id=pk).update(cprice=cprice1)
            Item.objects.filter(id=pk).update(sprice=sprice1)
            Item.objects.filter(id=pk).update(mrp=mrp1)
            Item.objects.filter(id=pk).update(tax=tax1)
            Item.objects.filter(id=pk).update(units=units1)
            Item.objects.filter(id=pk).update(stock=stock1)
            Item.objects.filter(id=pk).update(image=img)
            if u_form.is_valid():
                u_form.save()
                messages.success(
                    request, f"Item {title1} has been updated successfully"
                )
                return redirect("inventory")

        context = {"u_form": u_form, "item": instance1}

        return render(request, "inventory/item-update.html", context)
    else:
        messages.warning(request, f"Not an Admin")
        return redirect("/")


def delete(request, pk):
    title1 = Item.objects.get(id=pk).title
    Item.objects.filter(id=pk).delete()
    messages.success(request, f"Item {title1} has been delete successfully")
    return redirect("inventory")

