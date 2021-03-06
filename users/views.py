from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Customer, Deliveryguy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, CustomerCreateForm, DelvrygyCreateForm, CustUpdateForm, DeliveryguyUpdateForm


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


def delvrylist(request):
    if request.user.is_staff:
        context = {"dels": Deliveryguy.objects.all()}
        return render(request, 'users/delvry.html', context)
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
                return redirect('cust')
            else:
                context['form'] = form
                messages.warning(request, f'Customer {form.errors} creation failed')
                return render(request=request, template_name='users/create-cust.html', context=context)

        else:
            form = CustomerCreateForm()
            context['form'] = form
            return render(request=request, template_name='users/create-cust.html', context=context)
    else:
        messages.warning(request, f'Not an Admin')
        return redirect('/')

def deletecust(request, pk):
    title1 = Customer.objects.get(id=pk).name
    Customer.objects.filter(id=pk).delete()
    messages.success(request, f"Customer {title1} has been delete successfully")
    return redirect("cust")

def deletedelv(request, pk):
    title1 = Deliveryguy.objects.get(id=pk).name
    Deliveryguy.objects.filter(id=pk).delete()
    messages.success(request, f"Delivery {title1} has been delete successfully")
    return redirect("delv")

def createdelvry(request):
    context = {}
    if request.user.is_staff:
        if request.method == 'POST':
            form = DelvrygyCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                name = form.cleaned_data.get('name')
                messages.success(request, f'Delivery Guy {name} created successfully!')
                context['form'] = form
                return render(request=request, template_name='users/create-dlvry.html', context=context)
        else:
            form = DelvrygyCreateForm()
            context['form'] = form
            return render(request=request, template_name='users/create-dlvry.html', context=context)
    else:
        messages.warning(request, f'Not an Admin')
        return redirect('/')


def custupdate(request, pk):
    if request.user.is_staff:
        instance1 = get_object_or_404(Customer, id=pk)
        u_form = CustUpdateForm(request.POST, request.FILES, instance=instance1)
        if request.method == "POST":
            name1 = request.POST.get("name")
            email1 = request.POST.get("email")
            password1 = request.POST.get("password")
            addr1 = request.POST.get("address_line1")
            city1 = request.POST.get("address_line2")
            phone1 = request.POST.get("phone")
            zip_code1 = request.POST.get("zip_code")
            Customer.objects.filter(id=pk).update(name=name1)
            Customer.objects.filter(id=pk).update(email=email1)
            Customer.objects.filter(id=pk).update(password=password1)
            Customer.objects.filter(id=pk).update(address_line1=addr1)
            Customer.objects.filter(id=pk).update(address_line2=city1)
            Customer.objects.filter(id=pk).update(phone=phone1)
            Customer.objects.filter(id=pk).update(zip_code=zip_code1)
            if u_form.is_valid():
                u_form.save()
                messages.success(request, f"User {name1} has been updated successfully")
                return redirect("inventory")

        context = {"u_form": u_form, "cust": instance1}

        return render(request, "users/cust-update.html", context)
    else:
        messages.warning(request, f"Not an Admin")
        return redirect("/")


def delvryupdate(request, pk):
    if request.user.is_staff:
        instance1 = get_object_or_404(Deliveryguy, id=pk)
        u_form = DeliveryguyUpdateForm(request.POST, request.FILES, instance=instance1)
        if request.method == "POST":
            name1 = request.POST.get("name")
            email1 = request.POST.get("email")
            password1 = request.POST.get("password")
            addr1 = request.POST.get("address_line1")
            city1 = request.POST.get("address_line2")
            phone1 = request.POST.get("phone")
            zip_code1 = request.POST.get("zip_code")
            docname1 = request.POST.get("docname")
            Deliveryguy.objects.filter(id=pk).update(name=name1)
            Deliveryguy.objects.filter(id=pk).update(email=email1)
            Deliveryguy.objects.filter(id=pk).update(password=password1)
            Deliveryguy.objects.filter(id=pk).update(address_line1=addr1)
            Deliveryguy.objects.filter(id=pk).update(address_line2=city1)
            Deliveryguy.objects.filter(id=pk).update(phone=phone1)
            Deliveryguy.objects.filter(id=pk).update(zip_code=zip_code1)
            Deliveryguy.objects.filter(id=pk).update(docname=docname1)
            if u_form.is_valid():
                u_form.save()
                messages.success(request, f"Delivery Agent {name1} has been updated successfully")
                return redirect("inventory")

        context = {"u_form": u_form, "delv": instance1}

        return render(request, "users/delvry-update.html", context)
    else:
        messages.warning(request, f"Not an Admin")
        return redirect("/")
