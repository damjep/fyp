from django.urls import path
from .views import (
    updateFinanceReport,
    getFinanceList,
    FinanceReportChartAPIView,
    
    )

urlpatterns = [
    path('finance-api/get-report/', getFinanceList.as_view() ),
    path('finance-api/update-finance-report/', updateFinanceReport.as_view(), name='update-finance-report'),
    path('api/finance-report-chart/', FinanceReportChartAPIView.as_view(), name='finance-report-chart'),
]