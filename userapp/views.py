from multiprocessing import context
from re import template
from urllib import request
from django.shortcuts import redirect, render
#from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
#from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomerSignUpForm,EmployeeSignUpForm

def registration(request): 
    return render(request,'userapp/register.html')


def customer_register(request):
    if request.method == "POST":
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
                login(request, user)
                messages.success(request, 'Registration Successful')
                return redirect('homepage')
        messages.error(request, "Registration Unsuccessful. Invalid Data")
    form = CustomerSignUpForm()
    context = {'form':form}
    return render(request,'userapp/customer-register.html',context)


    
def employee_register(request):
    if request.method == "POST":
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
                login(request, user)
                messages.success(request, 'Registration Successful')
                return redirect('homepage')
        messages.error(request, "Registration Unsuccessful. Invalid Data")
    form = EmployeeSignUpForm()
    context = {'form':form}
    return render(request,'userapp/employee-register.html',context)

    
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username =username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                print(f'User Logged In As: ',request.user)
                if request.user.is_superuser:
                    return redirect('admin_dashboard')
                elif request.user.is_employee:
                    return redirect('employee_homepage')
                elif request.user.is_customer:
                    return redirect('homepage')
            else:
                messages.error(request, "Invalid Credentials!!!")
        else:
            messages.error(request, "Invalid Username or Password")
    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request,'userapp/login.html',context)


def user_logout(request):
    print(request)
    logout(request)
    messages.info(request, "You have successfully Logged Out.")
    return redirect('login')

##############################################################################################
#-------------Customer Registration using CreateView--------------------------------#
#from .forms import CustomerSignUpForm,EmployeeSignUpForm
#from django.views.generic import CreateView
#from django.urls import reverse
#from userapp.models import User

# class customer_register(CreateView):
#     model = User
#     form_class = CustomerSignUpForm
#     template_name = 'userapp/customer-register.html'
    
#     def get_success_url(self):
#         return reverse('homepage')
    
#     def validation(self,form):
#         user = form.save()
#         login(self,request,user)
#         return redirect('homepage')

#--------------------------Employee Registration using CreateView-------------------#

# class employee_register(CreateView):
#     model = User
#     form_class = EmployeeSignUpForm
#     template_name ='userapp/employee-register.html'

#     def get_success_url(self):
#         return reverse('homepage')
    
#     def validation(self,form):
#         user = form.save()
#         login(self,request,user)
#         return redirect('homepage')

####################################################################################################
