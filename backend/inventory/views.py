from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Inventory
from .serializers import inventorySerializer

class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = inventorySerializer
    permission_classes = [permissions.AllowAny]
# Create your views here.
