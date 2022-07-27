from django.shortcuts import render
from cartapp.models import *
from productapp.models import *
#Imports for api
from django.http import JsonResponse #To send json response
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from .serializers import OrderSerializers,CategorySerializers,UserTypeSerializers
from api import serializers

from rest_framework.authentication import TokenAuthentication #Import for implementing token authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

#for implementing token based response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
# from django.contrib.auth.models import User -------Since I've already custom user model into auth user model in settings, It'll cause an exception.
from django.contrib.auth import get_user_model



# Create your views here.

@api_view(['GET'])
def test_api(request):
    product_ordered = {
        'name':'Saleek',
        'age':'25',
        'Profession':'Software Developer'
    }
    return Response(product_ordered)

@api_view(['GET'])
def api_order(request):
    order = Order.objects.filter(complete = True)
    serializer = OrderSerializers(order, many = True)
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    return Response(serializer.data )

@api_view(['GET'])
def categoryList(request):
    category = Category.objects.all()
    serializer = CategorySerializers(category, many = True)
    return Response(serializer.data )

@api_view(['POST'])
def categoryCreate(request):
    serializer = CategorySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def categoryUpdate(request,pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializers(instance = category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def categoryDelete(request,pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response("Category Successfully Deleted!")


class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
        context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        

#Token Authentication
class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    User = get_user_model
    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
    
    
#Function based on token authentication    
@api_view(['GET'])
def user_type(request,pk):
    serializer = UserTypeSerializers(data=request.data)
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    user = User.objects.get(id = pk)
    # serializer = UserTypeSerializers(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    # return Response(serializer.data)
    if user.is_customer:
        return JsonResponse('Customer',safe=False)
    elif user.is_employee:
        return JsonResponse('Employee',safe=False)  
    if user.is_super:
        return JsonResponse('Super User',safe=False)  
    return JsonResponse('No Type for this particular user',safe=False)