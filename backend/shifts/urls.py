from django.urls import include, path, URLPattern, URLResolver
from .views import (
    getOrCreateShifts,
    getShiftsDays,
    getHours,
    getShiftTypes,
    UpdateShiftByID,
)


urlpatterns = [
    path('shifts/get-or-create-shifts', getOrCreateShifts.as_view(), name='getCreateShifts'),
    path('shifts/getShiftsDays', getShiftsDays.as_view(), name='getShiftsDays'),
    path('shifts/getHours', getHours.as_view(), name='getHours'),
    path('shifts/getShiftTypes', getShiftTypes.as_view(), name='get shift types'),
    path('shifts/update-shift/<int:pk>', UpdateShiftByID.as_view(), name='update'),
    
]
