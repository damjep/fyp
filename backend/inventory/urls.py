from django.urls import path
from .views import (
    InventoryList,
    EditInventoryItem,
)

urlpatterns = [
    path('stocks-api/get-stock-list/', InventoryList.as_view(), name='getList'),
    path('stocks-api/update-stocks/<int:id>/', EditInventoryItem.as_view()),
    
]
