from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('category-items/<int:pk>',views.category_items,name='category_items'),
    path('product_view/<int:pk>',views.product_view,name = 'product_view'),
]