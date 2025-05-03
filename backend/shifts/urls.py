from django.urls import include, path, URLPattern, URLResolver
from .views import (
    getOrCreateShifts,
    getShiftsDays,
    getHours,
    getShiftTypes,
    UpdateShiftByID,
    createUpdateShiftsAvailability,
    
)


urlpatterns = [
    path('shifts-api/get-or-create-shifts', getOrCreateShifts.as_view(), name='getCreateShifts'),
    path('shifts-api/getShiftsDays', getShiftsDays.as_view(), name='getShiftsDays'),
    path('shifts-api/getHours', getHours.as_view(), name='getHours'),
    path('shifts-api/getShiftTypes', getShiftTypes.as_view(), name='get shift types'),
    path('shifts-api/update-shift/<int:pk>', UpdateShiftByID.as_view(), name='update'),
    path('shifts-api/test/', createUpdateShiftsAvailability.as_view()),
]
