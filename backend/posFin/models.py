from django.db import models
from api.models import Dish
from django.core.exceptions import ValidationError

class Table(models.Model):
    tableNo = models.IntegerField(unique=True)
    max_seating = models.IntegerField()
    
    def __str__(self):
        return f"Table {self.tableNo}"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending' ,'pending'),
        ('paid' ,'paid'),
        ('cancelled' ,'cancelled'),
    ]
    
    ORDER_TYPES = [
        ('dine-in', 'dine-in'),
        ('takeaway', 'takeaway')
    ]
    
    order_number = models.CharField(max_length=20 )
    table_Number = models.ForeignKey(Table, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPES, default='dine-in')
    num_people = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tips = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def update_total_price(self):
        self.total_price = sum(item.total_price for item in self.orderitem_set.all())
        self.save(update_fields=['total_price']) 
        
    def clean(self):
        if self.order_type == 'dine-in':
            if self.num_people is None or self.num_people <= 0:
                raise ValidationError('Dine-in orders must have a positive number of people.')
            if self.table_Number is None:
                raise ValidationError('Dine-in orders must have an assigned table.')
        elif self.order_type == 'takeaway':
            if self.num_people and self.num_people > 0:
                raise ValidationError('Takeaway orders should not have a number of people.')
            if self.table_Number:
                raise ValidationError('TakeAway Cant be Seated')

        return super().clean()
            
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return f"{self.order_number}: {self.total_price}"
        
            
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    total_price = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    
    def save(self, *args, **kwargs):
        self.price = self.dish.price
        self.total_price = self.quantity*self.price
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.order}: Total: {self.total_price} Price: {self.price}"
        
class Payment(models.Model):
    PAYMENT_METHOD = [
        ('CASH', 'CASH'),
        ('CARD', 'CARD'), 
        ('ONLINE', 'ONLINE')
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=25, choices=PAYMENT_METHOD, default='CARD')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def update_status(self):
        self.order.status = 'paid'
        
    def revert_inventory(self):
        for order_item in self.order.orderitem_set.all():
            dish = order_item.dish
            inventory_item = dish.inventory_item

            if inventory_item:
                total_to_restore = order_item.quantity
                inventory_item.quantity += total_to_restore
                inventory_item.save(update_fields=['quantity'])


    def delete(self, *args, **kwargs):
        if self.order.status == 'paid':
            self.revert_inventory()
            self.order.status = 'pending'  # Or whatever your unpaid status is
            self.order.save(update_fields=['status'])
        super().delete(*args, **kwargs)

        
    def clean(self):
        if self.order.total_price > self.amount_paid:
            raise ValidationError("Amount Paid is Less")
        if self.amount_paid >= self.order.total_price:
            self.order.tips = self.amount_paid - self.order.total_price
            self.order.save(update_fields=['tips'])
        super().clean()
        
    def update_inventory(self):
        for order_item in self.order.orderitem_set.all():  
            dish = order_item.dish
            inventory_item = dish.inventory_item  

            if inventory_item:
                total_needed = order_item.quantity
                if inventory_item.quantity < total_needed:
                    raise ValidationError(f"Not enough stock for {inventory_item.name}")

                inventory_item.quantity -= total_needed
                inventory_item.save(update_fields=['quantity'])    
                
    def save(self, *args, **kwargs):
        is_new_payment = self._state.adding
        if not is_new_payment:
            # Existing payment being updated: first revert inventory
            if self.order.status == 'paid':
                self.revert_inventory()

        self.update_status()
        super().save(*args, **kwargs)
        self.order.save(update_fields=['status'])

        if self.order.status == 'paid':
            self.update_inventory()

        
    
        
    def __str__(self):
        return f"{self.order.table_Number}: {self.timestamp}"
        
    
    