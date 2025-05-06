from django.urls import path
from .views import ClockInAPIView, ClockOutAPIView, ClockStatusAPIView, UserClockedShiftSummaryAPIView

urlpatterns = [
    path('api/clock-in/', ClockInAPIView.as_view(), name='clock-in'),
    path('api/clock-out/', ClockOutAPIView.as_view(), name='clock-out'),
    path('api/clock-status/', ClockStatusAPIView.as_view(), name='clock-status'),
    path('api/clocked-shift-summary/', UserClockedShiftSummaryAPIView.as_view(), name='clocked-shift-summary'),
]
