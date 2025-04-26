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
    getOrCreatePayment,
    revert_payment,
    
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
    
    #paymentComponent
    path('pos-api/get-create-payment/', getOrCreatePayment.as_view() ),
    
    #past orders
    path('pos-api/revert-payment/<int:payment_id>/', revert_payment),
    
    #delete orderitems from order
    path('pos-api/<int:order_id>/items/<int:order_item_id>', deleteOrderItems.as_view())
]
