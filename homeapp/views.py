from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse, request
from django.db.models import Q
from productapp.models import Category, Product #Importing Product model from product app to home app
from django.core.paginator import Paginator #Pagination
# Create your views here.

def homepage(request):
    if 'searchbar' in request.GET:
        items = request.GET['searchbar']
        available_product = []
        #products = Product.objects.filter(product_name__icontains = items) #Single filtering
        products = Product.objects.filter(Q(product_brand__icontains = items)|Q(product_name__icontains = items))#Filtering multiple fields
        for product in products:
            if product in products and product.availability == True:
                available_product.append(product)
        products = available_product
        if not products:
            products = Product.objects.filter(category_name__category_name__contains = items) #first category_name denotes the field and second category_name denotes the return field of Category model
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products':products,'categories':categories}
    if request.user.is_authenticated:
        if request.user.is_employee:
            return render(request,'adminapp/employee_homepage.html',context)
        elif request.user.is_superuser:
            return render(request,'adminapp/superuser-dashboard.html',context)
    return render(request,'homeapp/homepage.html',context)


def category_items(request,pk):
    category = Category.objects.filter(id = pk)
    products = Product.objects.filter(category_name=category[0])
    categories = Category.objects.all()
    context = {'products':products,'categories':categories}
    return render(request,'homeapp/homepage.html',context)