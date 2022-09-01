from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from productapp.models import *
#from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
#signed_in_user = User.objects.filter(customer= request.user.customer)
# Create your views here.
def cart(request):
    if request.user.is_customer:
        customer = request.user
        signed_in_user = Order.objects.filter(customer= request.user)
        if signed_in_user:
            order,created = Order.objects.get_or_create(customer = request.user,complete = False)
            #order = Order.objects.filter(customer = customer,complete = False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total':0 , 'get_cart_items':0}
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0}
    context = {'items':items,'order':order}
    return render(request,'cartapp/cart.html',context)

def create_order(request,pk,customer):
    # order_obj = Order(customer=customer,transaction_id = '122334')
    order_obj = Order(customer=customer)
    order_obj.save()
    product_item = Product.objects.get(id = pk)
    incomplete_order = Order.objects.get(Q(customer = customer)&Q(complete = False))
    item_add = OrderItem(product = product_item,order = incomplete_order,quantity =1)
    item_add.save()

def add_to_cart(request,pk):
    if request.user.is_customer:
        customer = request.user
        try:
            incomplete_order = Order.objects.get(Q(customer = customer)&Q(complete = False))
        except Order.DoesNotExist:
            incomplete_order = None
        if incomplete_order:
            product_item = Product.objects.get(id = pk)
            item_present = OrderItem.objects.filter(product = pk,order = incomplete_order).values().first()
            print(item_present)
            #item_present = OrderItem.objects.filter(product = pk).values()[0]  --- use first() instead of [0] due to index out of range exception
            if item_present:
                item_quantity = item_present['quantity']
                item_update = OrderItem.objects.get(product = pk,order = incomplete_order)
                item_update.quantity = item_quantity + 1
                item_update.save()
            else:
                item_add = OrderItem(product = product_item,order = incomplete_order,quantity =1)
                item_add.save()
        else:
            create_order(request,pk,customer)
    return redirect('homepage')

def get_element(pk):
    item = OrderItem.objects.filter(id = pk).values().first() #Fetching the value item in cart
    item_quantity = item['quantity']
    item_obj = OrderItem.objects.get(id = pk) #Creating an object for OrderItem
    return item_obj,item_quantity

def add_cart_quantity(request,pk):
    if request.user.is_customer:
        item_obj,item_quantity = get_element(pk)
        item_obj.quantity = item_quantity + 1
        item_obj.save()
    return redirect('cart_list')


def reduce_cart_quantity(request,pk):
    if request.user.is_customer:
        item_obj,item_quantity = get_element(pk)
        if item_quantity == 1:
            item_obj.delete()
        else:
            item_obj.quantity = item_quantity - 1
            item_obj.save()
    return redirect('cart_list')

def remove_cart_item(request,pk):
    if request.user.is_customer:
        item_obj = get_element(pk)
        item_obj[0].delete()
        return redirect('cart_list')

def remove_cart(request):
    if request.user.is_customer:
        items = OrderItem.objects.all()
        items.delete()
    return redirect('cart_list')


def checkout(request):
    if request.user.is_authenticated:
        order = Order.objects.get(Q(customer = request.user)&Q(complete = False))
        order_items = OrderItem.objects.filter(order = order)
        categories = Category.objects.all()
        context = {'categories':categories,'order_items':order_items,'order':order}
    return render(request,'cartapp/checkout.html',context)


def create_checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.get(Q(customer = request.user)&Q(complete = False))
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        #user_name = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        zip = request.POST['zip']

        shipping_obj = ShippingAddress(customer = customer,order = order,first_name = first_name,last_name = last_name,email = email,address = address,country = country,state = state,zip_code = zip)
        shipping_obj.save()
        try:
            order_obj = Order.objects.get(Q(customer = request.user)&Q(complete = False))
            order_obj.complete = True
            order_obj.save()
        except Order.DoesNotExist:
            order_obj = None
    return redirect('homepage')

def wishlist_items(request,pk):
    if request.user.is_authenticated:
        product = Product.objects.get(id=pk)
        try:
            Wishlist_items = WishlistItem.objects.get(Q(customer = request.user)&Q(product = product))
        except WishlistItem.DoesNotExist:
            Wishlist_items = None
        if Wishlist_items:
            return('homepage')
        else:
            wishlist_obj = WishlistItem(customer = request.user,product = product)
            wishlist_obj.save()
            print(f"Product {product} Wishlisted")
            messages.info(request, f"You've wishlisted the product -  {product}")
    return redirect('homepage')

