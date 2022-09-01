from django.urls import path,include
from .import views

urlpatterns = [
    path('cart_list/',views.cart,name = 'cart_list'),
    path('cart-add/<int:pk>',views.add_to_cart,name = 'addcart'),
    path('add_cart_quantity/<int:pk>',views.add_cart_quantity, name='add_cart_quantity'),
    path('reduce_cart_quantity/<int:pk>',views.reduce_cart_quantity, name='reduce_cart_quantity'),
    path('remove_cart_item/<int:pk>',views.remove_cart_item,name='remove_cart_item'),
    path('remove_cart/',views.remove_cart,name='remove_cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('create_checkout/',views.create_checkout,name='create_checkout'),
    path('wishlisted/<int:pk>',views.wishlist_items,name='wishlisted'),
   # path('category-items/<int:pk>',views.category_items,name='category_items'),
]