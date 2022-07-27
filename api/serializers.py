from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers
from cartapp.models import *
from productapp.models import *

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name']
        

class UserTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name']