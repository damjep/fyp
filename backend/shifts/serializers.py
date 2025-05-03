from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from .models import Shift, ShiftAvailability

class ShiftAvailSerializer(ModelSerializer):
    shift_item_str = serializers.CharField(source='shift_item.__str__')
    class Meta:
        model = ShiftAvailability
        fields = ['user', 'shift_item', 'shift_item_str']
        read_only_fields = ['shift_item_str']
        
class ShiftAvailUpdateSerializer(ModelSerializer):
    class Meta:
        model = ShiftAvailability
        fields = ['user', 'shift_item']


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