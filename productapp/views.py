from email.message import Message
from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import ProductForm,CategoryForm
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger #Importing paginator for pagination.

# Create your views here.


def register_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        context = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'productapp/product-form.html',context)
    else:
        form = ProductForm()
        context = {'form':form}
        return render(request,'productapp/product-form.html',context)
    
def update_product(request,pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return redirect('homepage')
    form = ProductForm(instance = product)
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES, instance = product)
        if form.is_valid():
            form.save()
            messages.info(request, "Product Successfully Updated")
            return redirect('homepage')
    else:
        context = {'form':form}
        return render(request,'productapp/product-form.html',context)
    
def delete_product(request,pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return redirect('homepage')
    if request.method == 'POST':
        product.delete()
        messages.info(request,"Product Successfully Removed")
        return redirect('homepage')
    return render(request,'productapp/product-delete.html')


def register_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('category_index')
        else:
            return render(request,'productapp/category-form.html',context)
    else:
        form = CategoryForm()
        context = {'form':form}
        return render(request, 'productapp/category-form.html',context)
    

#Implementation of pagination while displaying category 
def category_index(request):
    categories_list = Category.objects.all().order_by('id')
    page = request.GET.get('page',1)
    paginator = Paginator(categories_list,10)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    context = {'categories':categories}
    return render(request,'productapp/category_index.html',context)


def category_update(request,pk):
    try:
        category = Category.objects.get(id = pk)        
    except Category.DoesNotExist:
        return redirect('homepage')
    form = CategoryForm(instance = category)
    if request.method == 'POST':
        form = CategoryForm(request.POST or None, instance=category)
        if form.is_valid():
            form.save()
            messages.info(request, "Category Successfully Updated")
            return redirect('category_index')
    else:        
        context = {'form':form}
        return render(request,'productapp/category-form.html',context)
    
    
def category_delete(request,pk):
    try:
        category = Category.objects.get(id = pk)
    except Category.DoesNotExist:
        return redirect('homepage')
    if request.method == 'POST':
        category.delete()
        messages.info(request,'Category Successfully Removed')
        return redirect('category_index')
    return render(request,'productapp/product-delete.html')
        