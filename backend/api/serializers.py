from rest_framework import serializers
from .models import User, Menu

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
            "is_active", "last_login",
            "groups", "user_permissions", 'role'
        ]
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
    
    
