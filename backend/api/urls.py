from django.urls import include, path, URLPattern, URLResolver
from typing import List

from .views import (
    LoginView,
    get_csrf_token,
    ProfileView,
    check_auth,
    MenuView,
    MenuViewEditor,
    DishEditor,
)

urlpatterns = [
    path('api/profile-view/', ProfileView.as_view(), name='profile-view'),
    path('api/login/',LoginView.as_view(), name='login'),
    path('get-token/', get_csrf_token ),
    path('api/check-auth/', check_auth, name='check_auth'),
    path('api/get-menu', MenuView.as_view(), name='menu-view'),
    path('api/edit-menu/<int:pk>', MenuViewEditor.as_view(), name='menu-edit'),
    path('api/edit-dish/<int:pk>', DishEditor.as_view(), name='dish-edit'),
    path('api/edit-dish/', DishEditor.as_view(), name='dish-edit'),

]
