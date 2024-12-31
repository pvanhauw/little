from django.shortcuts import render
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework import generics
# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

