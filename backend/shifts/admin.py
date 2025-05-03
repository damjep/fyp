from django.contrib import admin
from .models import Rota, Shift, ShiftAvailability

admin.site.register(Rota)
admin.site.register(Shift)
admin.site.register(ShiftAvailability)
# Register your models here.
