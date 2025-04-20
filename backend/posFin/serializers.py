from rest_framework import serializers
from .models import Table, Order, OrderItem
from api.models import Dish

class viewTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['tableNo', 'max_seating', 'id']
        
class addOrderByTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
        
    def create(self, validated_data):
        order_number = validated_data.get('order_number')
        num_people = validated_data.get('num_people')
        table_Number = validated_data.get('table_Number')
        
        return Order.objects.create(
            order_number = order_number,
            num_people = num_people,
            table_Number = table_Number,
        )
        
        
## tabViewModal
class orderItemsPerIdSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(source='order.id')
    dish_name = serializers.CharField(source='dish.name')
    order_tableNo = serializers.CharField(source='order.table_Number')
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'dish', 'order_tableNo',
                  'dish_name', 'quantity', 'price', 'total_price']
        
class addOrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'dish', 'quantity', 'price', 'total_price']
        read_only_fields = ['id', 'order', 'price', 'total_price']

    def create(self, validated_data):
        order = self.context.get('order')
        if not order:
            raise serializers.ValidationError("Order not found in context")

        return OrderItem.objects.create(
            order=order,
            dish=validated_data['dish'],
            quantity=validated_data['quantity'],
            price=validated_data['dish'].price,
            total_price=validated_data['dish'].price * validated_data['quantity']
        )
