from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Customer, Deliveryguy
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from inventory.models import Orders
from datetime import datetime ,date, timedelta

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


"""class ChartData(APIView):
"View to list all users in the system.
* Requires token authentication.
* Only admin users are able to access this view."
authentication_classes = []
permission_classes = []
def get(self, request, format1=None):
    qs_count = User.objects.all().count()
    labels = [user.username for user in User.objects.all()]
    labels2 = [post.id for post in Orders.objects.all()]
    default_items = [Orders.objects.filter(id=user.id).count() for user in User.objects.all()]
    colors = []
    colors2 = []
    allhits = []
    for user in User.objects.all():
        color ='rgba('+format(random.randint(0,255))+","+format(random.randint(0,255))+","+format(random.randint(0,255))+",1)"
        colors.append(color)
    for post in Orders.objects.all():
        hit9 = Deliveryguy.objects.get(id = post.pk)
        noofhits = hit9.id
        allhits.append(noofhits)
    for post in Orders.objects.all():
        color ='rgba('+format(random.randint(0,255))+","+format(random.randint(0,255))+","+format(random.randint(0,255))+",1)"
        colors2.append(color)
    data = {
                "labels": labels,
                "default": default_items,
                "bgcolor": colors,
                "labels2": labels2,
                "bgcolor2": colors2,
                "defaultviews": allhits,

            }
    ##usernames = [user.username for user in User.objects.all()]
    return Response(data)"""

class ChartData(APIView):
    """
    View to list all users in the system.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format1=None):
        qs_count = Customer.objects.all().count()
        #labels = [user.username for user in User.objects.all()]
        #labels2 = [post.id for post in Orders.objects.all()]
        #default_items = [Orders.objects.filter(id=user.id).count() for user in User.objects.all()]
        count =0
        tot = 0
        print(datetime.now().date().today())
        li = []
        for i in reversed(range(30)):
            yesterday = date.today() - timedelta(days=i)
            count = 0
            for order in Orders.objects.all():
                a = order.created_at.date()
                
                if (a == yesterday):
                    count = count+1
                    tot = tot +1
                    print("Orders On",yesterday," are ",count)  
                 
            li.append(count) 
        print("List Elements:",li)    
        print("Total Orders",tot)
        #orders = [Orders.objects.filter(created_at=datetime.date().today()).count()]
        #dt= Orders.objects.get(created_at=)
         
        colors = []
        default_items = [2,34,55,3]
        colors2 = []
        labels = [1,2,3,4]
        allhits = []
        for user in User.objects.all():
            color ='rgba('+format(random.randint(0,255))+","+format(random.randint(0,255))+","+format(random.randint(0,255))+",1)"
            colors.append(color)
        '''for post in Orders.objects.all():
            hit9 = Deliveryguy.objects.get(id = post.pk)
            noofhits = hit9.id
            allhits.append(noofhits)'''
        data = {
                 "labels": labels,
                 "default": default_items,
                 "bgcolor": colors,
                 "order1":li
                }
        ##usernames = [user.username for user in User.objects.all()]
        return Response(data)