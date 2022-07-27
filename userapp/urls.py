from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('logout/',views.user_logout,name='logout'),
    path('customer-register/',views.customer_register,name='customer_register'),
    path('employee-register/',views.employee_register,name='employee_register'),
]


#View url for class based registration
#path('customer-register/',views.customer_register.as_view(),name='customer_register'),
#path('employee-register/',views.employee_register.as_view(),name='employee_register'),
