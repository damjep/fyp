from rest_framework import serializers
from .models import User, Category, Dish, DishType
from shifts.serializers import ShiftSerializer
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


class ListUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id',"name", "email", "role", "password"]
        read_only_fields = ['id',]
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # hash password
        user.save()
        return user
        
class UpdateUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name', 'email', 'role']
        read_only_fields = ['id']     
    
# Shifts Available Users
class UpdateShiftsSerializer(serializers.ModelSerializer):    
    class Meta: 
        model = User
        fields = ['id', 'name', 'email', 'shift_available']
        read_only_fields = ['id', 'name', 'email']

class ListShiftsAvailabilitySerializer(serializers.ModelSerializer):
    shift_available = ShiftSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'shift_available']
        read_only_fields = ['id', 'name', 'email']

        
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
    id = serializers.IntegerField(required=True)
    
    class Meta:
        model = Dish
        fields = "__all__"
    
    
class MenuEditSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    
    class Meta:
        model = Category
        fields = ['id', 'dish_type', 'dishes' ]
        
    def create_or_update_dishes(self, dishes):
        dishes_id = []
        for dish in dishes:
            if 'id' not in dish:
                dish_instance, created = Dish.objects.update_or_create(name=dish['name'], defaults=dish)
            else:
                dish_instance , created = Dish.objects.update_or_create(pk=dish['id'], defaults=dish)
            dishes_id.append(dish_instance.pk)
            
        return dishes_id
    
    def get_or_create_dishes(self, dishes):
        dishes_id = []
        for dish in dishes:
            dish_instance , created = Dish.objects.get_or_create(pk=dish['id'], defaults=dish)
            dishes_id.append(dish_instance.pk)
            
        return dishes_id
    
    def create(self, validated_data):
        dishes = validated_data.pop('dishes', [])
        category = Category.objects.create(**validated_data)
        category.dishes.set(self.get_or_create_dishes(dishes))
        return category
    
    def update(self, instance, validated_data):
        dishes = validated_data.pop('dishes', [])
        instance.dishes.set(self.create_or_update_dishes(dishes))

        fields = ['name', 'description', 'price']
        for field in fields:
            if field in validated_data:  # ✅ Ensure the field exists
                setattr(instance, field, validated_data[field])
        
        instance.save()
        return instance
    
class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    dish_type = DishTypeSerializer(read_only=False)
    
    class Meta:
        model = Category
        fields = ['id', 'dish_type', 'dishes' ]
        
    def update(self, instance, validated_data):
        dishes = validated_data.get('dishes')
        dish_type_data = validated_data.get('dish_type')

        # ✅ Handle ForeignKey dish_type correctly
        if dish_type_data and isinstance(dish_type_data, dict):
            dish_type_id = dish_type_data.get('id')
            if dish_type_id:
                try:
                    dish_type_instance = DishType.objects.get(id=dish_type_id)
                    dish_type_instance.name = dish_type_data.get("name", dish_type_instance.name)
                    dish_type_instance.extra_dish_type = dish_type_data.get("extra_dish_type", dish_type_instance.extra_dish_type)
                    dish_type_instance.save()

                    instance.dish_type = dish_type_instance  # Assign updated instance
                    
                except DishType.DoesNotExist:
                    raise serializers.ValidationError({"dish_type": "Invalid dish type ID."})
            else:
                raise serializers.ValidationError({"dish_type": "Dish type ID is required."})

                               
        for dish in dishes:
            dish_id = dish.get('id', None)
            if dish_id: 
                dish_item = Dish.objects.get(id=dish_id)
                dish_item.name = dish.get('name', dish_item.name)
                dish_item.price = dish.get('price', dish_item.price)
                dish_item.description = dish.get('description', dish_item.description)
                dish_item.save()
                
            else:
                dish_item = Dish.objects.create(**dish)
                instance.dishes.add(dish_item)
                
        
        instance.save()
        return instance
            
class CategoryListSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    dish_type = DishTypeSerializer(read_only=False)
    
    class Meta:
        model = Category
        fields = ['id', 'dish_type', 'dishes' ]
        
    def get_or_create_dishes(self, dishes):
        dishes_id = []
        for dish in dishes:
            dish_instance , created = Dish.objects.get_or_create(pk=dish['id'], defaults=dish)
            dishes_id.append(dish_instance.pk)
            
        return dishes_id    
    
    def create(self, validated_data):
        dish_type_data = validated_data.pop('dish_type', None)
        dishes = validated_data.pop('dishes', [])

        # If dish_type exists, retrieve or create it
        dish_type = None
        if dish_type_data:
            dish_type, _ = DishType.objects.get_or_create(name=dish_type_data['name'], extra_dish_type=dish_type_data['extra_dish_type'])

        # Create Category with or without dish_type
        category = Category.objects.create(dish_type=dish_type, **validated_data)

        # Assign dishes to the created category
        category.dishes.set(self.get_or_create_dishes(dishes))

        return category
    
class UserShiftsOnlySerializer(serializers.ModelSerializer):
    shift_available = serializers.SerializerMethodField()  # Change to SerializerMethodField

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'shift_available']

    
    

    