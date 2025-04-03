from django.shortcuts import render
from django.http import request, JsonResponse
from .models import Order

def getStatusChoices(request):
    if request.method == 'GET':
        status_choices = dict(Order.STATUS_CHOICES)
        dine_type = dict(Order.ORDER_TYPES)
        return JsonResponse({'status_choices': status_choices, 'order_type': dine_type})

# Create your views here.
