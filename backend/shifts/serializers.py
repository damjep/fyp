from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from .models import Shift, ShiftAvailability, Rota

## Shift Availability
class ShiftAvailSerializer(ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_role = serializers.CharField(source='user.role', read_only=True)
    shift_item_type = serializers.CharField(source='shift_item.shift_type')
    shift_item_days = serializers.CharField(source='shift_item.days')
    shift_item_str = serializers.CharField(source='shift_item.__str__')
    class Meta:
        model = ShiftAvailability
        fields = ['user', 'shift_item', 'shift_item_str', 'id', 'user_role',
                  'shift_item_days', 'shift_item_type', 'user_name']
        read_only_fields = ['shift_item_str', 'id',
                            'shift_item_days', 'shift_item_type']
        
class ShiftAvailUpdateSerializer(ModelSerializer):
    class Meta:
        model = ShiftAvailability
        fields = ['user', 'shift_item', 'id']
        read_only_fields = ['id']
        
## Rota 
class RotaSerializer(serializers.ModelSerializer):
    shifts_detail = ShiftAvailSerializer(source='shifts', many=True,
                                         read_only= True)
    class Meta:
        model = Rota
        fields = ['start_date', 'end_date', 'shifts', 'id',
                  'shifts_detail']
        read_only_fields = ['id']
        

## Shifts
class ShiftSerializer(ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'
        
class DaySerializer(Serializer):
    key = serializers.CharField()
    value = serializers.CharField()
    
class HourSerializer(Serializer):
    key = serializers.CharField()
    value = serializers.CharField()
    
class ShiftTypeSerializer(Serializer):
    key = serializers.CharField()
    value = serializers.CharField()