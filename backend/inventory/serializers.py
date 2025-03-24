from rest_framework import serializers
from .models import Inventory

class inventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"