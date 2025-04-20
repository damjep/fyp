from django.shortcuts import render, get_object_or_404
from django.http import request, JsonResponse
from .models import Order, Table, OrderItem
from rest_framework import generics, permissions
from .serializers import (viewTableSerializer, 
                          addOrderByTableSerializer, 
                          orderItemsPerIdSerializer,
                          addOrderItemsSerializer)
from rest_framework import serializers

def getStatusChoices(request):
    if request.method == 'GET':
        status_choices = dict(Order.STATUS_CHOICES)
        dine_type = dict(Order.ORDER_TYPES)
        return JsonResponse({'status_choices': status_choices, 'order_type': dine_type})


def get_active_table_numbers(request):
    active_orders = Order.objects.filter(status='pending').select_related('table_Number')

    data = [
        {
            'order_id': order.id,
            'table_number': order.table_Number.tableNo,
        }
        for order in active_orders
    ]

    return JsonResponse({'active_orders': data})

class getOrderByID(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = addOrderByTableSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_object(self):
        return get_object_or_404(Order, id=self.kwargs['pk'])
    
class viewTableList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = viewTableSerializer
    permission_classes = [permissions.AllowAny]
    
class editTableByID(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = viewTableSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_object(self):
        return get_object_or_404(Table, id=self.kwargs['pk'])
    
class addOrderByTable(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = addOrderByTableSerializer
    permission_classes = [permissions.AllowAny]
            
    
## tabViewModal
class getOrderItems(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return addOrderItemsSerializer
        return orderItemsPerIdSerializer

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return OrderItem.objects.filter(order__id=order_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        try:
            order = Order.objects.get(pk=self.kwargs['order_id'])
        except Order.DoesNotExist:
            raise serializers.ValidationError("Order not found")
        context['order'] = order
        return context

# delete list order items 
class deleteOrderItems(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = orderItemsPerIdSerializer
    
    def get_queryset(self):
        return OrderItem.objects.all()
    
    def get_object(self):
        order_item_id = self.kwargs['order_item_id']
        return get_object_or_404(OrderItem, pk=order_item_id)

