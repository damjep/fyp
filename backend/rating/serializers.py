from rest_framework import serializers
from .models import Rating

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['name', 'rating', 'comment', 'id']
        read_only_fields = ['id']