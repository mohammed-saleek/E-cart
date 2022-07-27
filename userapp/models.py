# from django.db import models
# from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.




# class UserManager(BaseUserManager):
#     def _create_user(self,email,password,is_staff,is_superuser,**extra_fields):
#         if not email:
#             raise ValueError('Users Must Have An Email Address')
#         now = timezone.now()
#         email = self.normalize_email(email)
#         user = self.model(email = email,is_staff = is_staff,is_active = True,is_superuser = is_superuser,last_login = now, date_joined = now,**extra_fields)
#         user.set_password(password)
#         user.save(using = self._db)
#         return user
    
#     def create_user(self,email=None,password=None,**extra_fields):
#         return self._create_user(email,password,False,False,**extra_fields)
    
#     def create_user(self,email,password,**extra_fields):
#         user = self._create_user(self,email,password,**extra_fields)
#         user.save(using = self._db)
#         return user
    
    
# class User(AbstractUser,PermissionsMixin):
#     email = models.EmailField(max_length=100,unique=True)
#     name = models.CharField(max_length=200,null=True,blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active: models.BooleanField(default=True)
#     last_login = models.DateTimeField(null=True,blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
    
#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def get_absolute_url(self):
#         return "/users/%i/" % (self.pk)
#     def get_email(self):
#         return self.email


# class user_type(models.Model):
#     is_admin = models.BooleanField(default=False)
#     is_customer = models.BooleanField(default=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         if self.is_customer == True:
#             return User.get_email(self.user) + " - is_customer"
#         else:
#             return User.get_email(self.user) + " - is_admin"







# from django.db.models.signals import post_save

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    phone_no = models.CharField(max_length=13)
    country = models.CharField(max_length=25)
    last_login =models.DateTimeField(auto_now_add=True, blank=True)
    
    #def __str__(self):
    #    return self.user

class Employee(models.Model):
    #designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    # designation = (('Jr Software Engineer','Jr Software Engineer'),
    #     ('Sr Software Engineer','Sr Software Engineer'),
    #     ('Operations Manager','Operations Manager'),
    #     ('Sales Executive','Sales Executive'),
    #     ('Project Manager','Project Manager'),
    #     ('CEO','CEO'))
    #designation = models.CharField(max_length=50,choices=designation,null=True)
    designation = models.CharField(max_length=50)
    city = models.CharField(max_length=40)
    last_login =models.DateTimeField(auto_now_add=True, blank=True)
    
    #def __str__(self):
        #return self.user
    

# @receiver(post_save,sender = User)
# def create_user_profile(sender,instance,created,**kwargs):
#     print("********",created)
#     if instance.is_customer:
#         Customer.objects.get_or_create(user = instance)
#     if instance.is_employee:
#         Employee.objects.get_or_create(user = instance)


# @receiver(post_save,sender = User)
# def save_user_profile(sender,instance,**kwargs):
#     print('------')
#     if instance.is_customer:
#         instance.Customer.save()
#     if instance.is_employee:
#         instance.Employee.save()

#########################################
# class UserAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if request.user.is_staff:
#             obj.is_superuser = True
#             obj.save()

