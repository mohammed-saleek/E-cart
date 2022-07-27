from django.shortcuts import render
from userapp.models import *
from productapp.models import *
from cartapp.models import *
from datetime import *
# Create your views here.
def admin_dashboard(request):
    user_count = User.objects.all().count()
    total_orders = Order.objects.filter(complete = True).count()
    orders = Order.objects.filter(complete = True)
    # for i in orders:
    #     print(datetime.date(i.date_ordered))
        
    # month = datetime.now().month
    # print(str(month))
    # year = datetime.now().year
    # print(str(year))
    # items = Order.objects.raw("Select * from cartapp_Order where complete = true and date_ordered like '%{year}-0{month}%;'")
    # items = Order.objects.filter
    # for i in items:
    #         print(i)

    context = {'user_count':user_count,'total_orders':total_orders}
    return render(request,'adminapp/superuser-dashboard.html',context)


def employee_panel(request):
    user = request.user
    products = Product.objects.filter(availability = True)
    context = {'user':user,'products':products}
    return render(request,'adminapp/employee_homepage.html',context)