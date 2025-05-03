from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Inventory
from .serializers import inventorySerializer

class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = inventorySerializer
    permission_classes = [permissions.AllowAny]
    
class EditInventoryItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = inventorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        inventory_id = self.kwargs['id']
        return Inventory.objects.get(pk=inventory_id)
# Create your views here.
