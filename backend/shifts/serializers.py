from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from .models import Shift

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