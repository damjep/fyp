from rest_framework import serializers
from .models import User, Category, Dish, DishType
from django.shortcuts import get_object_or_404

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        """
        Custom validation to ensure the email exists and password is correct.
        """
        email = data.get("email")
        password = data.get("password")

        user = User.objects.filter(email=email).first()

        if user is None:
            raise serializers.ValidationError("User with this email does not exist.")
        
        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password.")
        
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "email", "is_staff", "is_superuser",
            "is_active", "last_login", 'name',
            "groups", "user_permissions", 'role', 'role'
        ]
        

        
class DishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishType
        fields = "__all__"
        
class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"
    
class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    dish_type = DishTypeSerializer()
    
    class Meta:
        model = Category
        fields = ['id', 'dish_type', 'extra_dish_type', 'dishes' ]
        
    def update(self, instance, validated_data):
        dishes_data = validated_data.get('dishes')
        
        
        for dish_data in dishes_data:
            dish = get_object_or_404(Dish, pk=dish_data.get('id'))
            dish.name = dish_data.get('name')
            dish.price = dish_data.get('price')
            dish.save()
        
        instance.save()
        
        return instance
            
