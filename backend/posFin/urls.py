from django.urls import path
from .views import (
    getStatusChoices,
    viewTableList,
    editTableByID,
    addOrderByTable,
    getOrderByID,
    get_active_table_numbers,
    getOrderItems,
    deleteOrderItems,
)

urlpatterns = [
    path('pos-api/get-order-enum/', getStatusChoices),
    path('pos-api/get-table-list/', viewTableList.as_view()),
    path('pos-api/edit-table/<int:pk>', editTableByID.as_view()),
    path('pos-api/add-order-by-table/', addOrderByTable.as_view()),
    path('pos-api/get-order-by-id/<int:pk>', getOrderByID.as_view()),
    path('pos-api/get-active-tables', get_active_table_numbers),
    
    ## tabViewModel
    path('pos-api/<int:order_id>/items/', getOrderItems.as_view()),
    
    #delete orderitems from order
    path('pos-api/<int:order_id>/items/<int:order_item_id>', deleteOrderItems.as_view())
]
