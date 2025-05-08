from rest_framework import serializers
from .models import Table, Order, OrderItem, Payment
from api.models import Dish

class viewTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['tableNo', 'max_seating', 'id']
        
class addOrderByTableSerializer(serializers.ModelSerializer):
    table_no_str = serializers.CharField(source='table_Number.tableNo', read_only=True)
    class Meta:
        model = Order
        fields = ['order_number', 'table_Number', 'table_no_str',
                  'created_at', 'id', 'order_type', 'num_people'
                  ,'status','total_price', 'service_charge', 'tips' ]
        read_only_fields = ['id', 'created_at']
        
    def create(self, validated_data):
        order_type = validated_data.get('order_type')
        if order_type == 'dine-in':
            order_number = validated_data.get('order_number')
            num_people = validated_data.get('num_people')
            table_Number = validated_data.get('table_Number')
            
            return Order.objects.create(
                order_number = order_number,
                num_people = num_people,
                table_Number = table_Number,
            )
            
        if order_type == 'takeaway':
            order_number = validated_data.get('order_number')
            num_people = validated_data.get('num_people')
            
            return Order.objects.create(
                order_number = order_number,
                num_people = num_people,
                order_type = order_type
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
        
## payment 
class getOrCreatePayment(serializers.ModelSerializer):
    order_created_at = serializers.DateTimeField(source='order.created_at', read_only=True)
    order_dine_type = serializers.CharField(source='order.order_type', read_only = True)
    order_number = serializers.CharField(source='order.order_number', read_only=True)
    
    class Meta:
        model = Payment
        fields = ['id', 'order', 'payment_method', 'amount_paid', 
                  'order_created_at', 'order_dine_type', 'timestamp',
                  'order_number']
        read_only_fields = ['timestamp']
        
    def create(self, validated_data):
        order = validated_data.get('order')
        payment_method = validated_data.get('payment_method')
        amount_paid = validated_data.get('amount_paid')
        
        return Payment.objects.create(
            order = order,
            payment_method = payment_method,
            amount_paid = amount_paid,
        )

        
