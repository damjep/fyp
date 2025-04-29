from rest_framework.serializers import Serializer
from rest_framework import serializers
from .models import FinanceReport

class ListFinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceReport
        fields = ['id','date', 'total_sales', 'total_tips', 'total_service_charge']
        read_only_fields = ['id']