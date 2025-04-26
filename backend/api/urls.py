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
    GetDishTypesView,
    ListMenuRawView,
    EditDishTypesView,
    MenuListViewEditor,
    viewAllUserShiftAvailability,
    LogoutView,
)

urlpatterns = [
    path('api/profile-view/', ProfileView.as_view(), name='profile-view'),
    path('api/login/',LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view()),
    path('get-token/', get_csrf_token ),
    path('api/check-auth/', check_auth, name='check_auth'),
    path('api/get-menu', MenuView.as_view(), name='menu-view'),
    path('api/edit-menu/<int:pk>', MenuViewEditor.as_view(), name='menu-edit'),
    path('api/edit-dish/<int:pk>', DishEditor.as_view(), name='dish-edit'),
    path('api/edit-dish/', DishEditor.as_view(), name='dish-edit'),
    path('api/get-dish-types', GetDishTypesView.as_view(), name='fetch-dish-types'),
    path('api/get-list-raw', ListMenuRawView.as_view(), name='list-raw'),
    path('api/edit-dish-types/<int:pk>', EditDishTypesView.as_view()),
    path('api/menu-list-editor/', MenuListViewEditor.as_view()),
    path('api/get-users-shift-availability', viewAllUserShiftAvailability.as_view(), name='get-users-shift-availability'),
]
