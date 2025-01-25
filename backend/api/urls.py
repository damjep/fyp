from django.urls import include, path, URLPattern, URLResolver
from typing import List

from .views import (
    LoginView,
    get_csrf_token,
    ProfileView,
)

urlpatterns = [
    path('api/profile-view/', ProfileView.as_view(), name='profile-view'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('get-token/', get_csrf_token )
]
