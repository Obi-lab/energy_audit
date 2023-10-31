from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import (MyTokenObtainPairSerializer, 
                          RegisterSerializer,UserDetailsSerializer)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import UserAccount
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = UserAccount.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def profile_update(request):
    user = request.user  

    try:
        user_details = UserAccount.objects.get(user=user)
        
    except UserAccount.DoesNotExist:
        return Response({'detail': 'User details not found.'}, status=status.HTTP_404_NOT_FOUND)
        

    data = {
        'name': request.data.get('name', user_details.name),
        #'cover_photo': request.data.get('cover_photo', user_details.cover_photo)
    }
    
    serializer = UserDetailsSerializer(user_details, data=data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_get(request):
    email = request.user.email

    try:
        user_details = UserAccount.objects.get(email=email)
    except UserAccount.DoesNotExist:
        return Response({'detail': 'User details not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserDetailsSerializer(user_details)
    
    return Response(serializer.data)


    
    
