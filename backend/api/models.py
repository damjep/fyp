from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from typing import Optional
from django.apps import apps
from inventory.models import Inventory


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: Optional[str] = None, **extra_fields: dict) -> "User":
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user: User = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: Optional[str] = None, **extra_fields: dict) -> "User":
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email: str) -> "User":
        return self.get(email=email)
    

class DishType(models.Model):
    name = models.CharField(max_length=100)
    extra_dish_type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name  + " " + self.extra_dish_type  
     
class Category(models.Model):
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, blank=True)
    dishes = models.ManyToManyField('Dish', related_name='dishes')
    
    def __str__(self):
        return str(self.dish_type)
    
    
class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        MANAGER = 'Manager'
        EMPLOYEE = 'Employee'
        KITCHEN_STAFF = 'Kitchen Staff'
    
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.EMPLOYEE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    shift_available = models.ManyToManyField('shifts.Shift', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    