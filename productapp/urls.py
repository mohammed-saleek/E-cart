from django.urls import URLPattern, path,include
from . import views

urlpatterns = [
    path('product-registration/', views.register_product, name='register_product'),
    path('product-update/<int:pk>',views.update_product,name='update_product'),
    path('product-delete/<int:pk>',views.delete_product, name = 'delete_product'),
    path('register_category/',views.register_category,name='register_category'),
    path('all-categories/',views.category_index,name='category_index'),
    path('category-update/<int:pk>',views.category_update,name='category_update'),
    path('category-remove/<int:pk>',views.category_delete,name='category_delete'),
]