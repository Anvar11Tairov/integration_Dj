from django.shortcuts import render
from rest_framework import generics
from .models import MyUsers
from .serializers import UserSerializer

class UsersApiView(generics.ListAPIView):
    queryset = MyUsers.objects.all()
    serializer_class = UserSerializer

