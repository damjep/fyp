from django.contrib import admin
from .models import Order, OrderItem, Table, Payment

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Table)
admin.site.register(Payment)
# Register your models here.
