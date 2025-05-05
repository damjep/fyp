from django.urls import include, path, URLPattern, URLResolver
from .views import (
    AverageRatingAPIView,
    getCreateRatingList,
    
)

urlpatterns = [
    path('ratings-api/get-avg-rating/', AverageRatingAPIView.as_view()),
    path('ratings-api/get-create-list/', getCreateRatingList.as_view()),
]
