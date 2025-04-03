from django.urls import path
from .views import (
    getStatusChoices,
)

urlpatterns = [
    path('pos-api/get-order-enum/', getStatusChoices),
    
]
