from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('category-items/<int:pk>',views.category_items,name='category_items'),
]