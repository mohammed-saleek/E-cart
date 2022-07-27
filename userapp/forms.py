from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from .models import Customer,Employee,User

#Create your form here

# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
    
#     class Meta:
#         model = User
#         fields = ("username","email","is_staff","password1","password2")
        
#         def save(self, commit=True):
#             user = super(NewUserForm,self).save(commit=False)
#             user.email = self.cleaned_data['email']
#             if commit:
#                 user.save()
#             return user


# class TestUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)  
#     class Meta:
#         model = User
#         fields = '__all__'  



# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
        
# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'
        
# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = '__all__'


class CustomerSignUpForm(UserCreationForm):
    phone_no = forms.CharField(required=True)
    country = forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_no = self.cleaned_data.get('phone_no')
        customer.country = self.cleaned_data.get('country')
        customer.save()
        return customer


class EmployeeSignUpForm(UserCreationForm):
    # designation_choices = (('Jr Software Engineer','Jr Software Engineer'),
    #     ('Sr Software Engineer','Sr Software Engineer'),
    #     ('Operations Manager','Operations Manager'),
    #     ('Sales Executive','Sales Executive'),
    #     ('Project Manager','Project Manager'),
    #     ('CEO','CEO'))
    #designation = forms.MultipleChoiceField(widget=forms.Select,choices=designation_choices)
    designation = forms.CharField(required=True)
    city = forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.designation = self.cleaned_data.get('designation')
        employee.city = self.cleaned_data.get('city')
        employee.save()
        return employee