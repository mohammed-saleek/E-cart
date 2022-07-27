from django.urls import URLPattern, path,include
from .import views

urlpatterns = [
    path('test_api/',views.test_api,name='test_api'),
    path('api_ordered_orders/',views.api_order,name='api_order'),
    path('category-create/',views.categoryCreate,name='category_create'),
    path('category-list/',views.categoryList,name='category_create'),
    path('category-update/<int:pk>',views.categoryUpdate,name='category_update'),
    path('category-delete/<int:pk>',views.categoryDelete,name='category_delete'),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('api-list-users-token_auth/', views.ListUsers.as_view()),
    path('api-user-type/<int:pk>',views.user_type,name='user_type'),
    
]