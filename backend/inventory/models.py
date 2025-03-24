from django.db import models

class Inventory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    quantity = models.DecimalField(max_digits=3, decimal_places=0)
    
    def __str__(self):
        return f"{self.name}: {self.quantity}"
    
    
# Create your models here.
