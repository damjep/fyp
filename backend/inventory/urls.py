from django.urls import path
from .views import (
    InventoryList
)

urlpatterns = [
    path('stocks/get-stock-list', InventoryList.as_view(), name='getList'),
    
]
