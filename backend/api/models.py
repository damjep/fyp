from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from typing import Optional

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
    
class Shift(models.Model):
    class Shift_Type(models.TextChoices):
        AM = 'AM'
        PM = 'PM'
        
    class Days(models.TextChoices):
        MONDAY = 'Monday'
        TUESDAY = 'Tuesday'
        WEDNESDAY = 'Wednesday'
        THURSDAY = 'Thursday'
        FRIDAY = 'Friday'
        SATURDAY = 'Saturday'
        SUNDAY = 'Sunday'
        
    HOURS = [(i, f"{i}:00") for i in range(24)]  # Choices from 0 to 23
    
    shift_start = models.IntegerField( choices=HOURS, default=HOURS[0])
    shift_end = models.IntegerField( choices=HOURS, blank=True )
    days = models.CharField(max_length=20,
                             choices=Days.choices, 
                             default=Days.MONDAY)
    shift_type = models.CharField(max_length=2, 
                                  choices=Shift_Type.choices, 
                                  default='AM')
    
    def __str__(self):
        return f"{self.days} {self.shift_type} from {self.shift_start}:00 to {self.shift_end}:00"

class DishType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name   
     
class Category(models.Model):
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, blank=True)
    extra_dish_type = models.CharField(max_length=100, blank=True)
    dishes = models.ManyToManyField('Dish', related_name='dishes')
    
    def __str__(self):
        return self.dish_type.name + self.extra_dish_type 
    

    
class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        MANAGER = 'Manager'
        EMPLOYEE = 'Employee'
    
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.EMPLOYEE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    shift_available = models.ManyToManyField('Shift', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email


    