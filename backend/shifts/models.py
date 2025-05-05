from django.db import models
from django.contrib.auth import get_user_model
from django import forms
from django.db.models.signals import post_delete
from django.dispatch import receiver

User = get_user_model()
    
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
    max_employee = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.days} {self.shift_type} from {self.shift_start}:00 to {self.shift_end}:00"
    
class ShiftAvailability(models.Model):
    shift_item = models.ForeignKey(Shift, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
        
    def __str__(self):
        return f"{self.user.name} - {self.shift_item}"
    
class Rota(models.Model):
    start_date = models.DateField(blank=True, null=True, unique=True)
    end_date = models.DateField(blank=True, null=True, unique=True)
    shifts = models.ManyToManyField(ShiftAvailability)

    def __str__(self):
        return f"Week {self.start_date} - {self.end_date}"
        