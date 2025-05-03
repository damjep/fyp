from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
import logging
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from typing import Dict, Any
import json
from rest_framework.views import APIView
from .serializers import (
    LoginSerializer, UserSerializer, 
    CategoryListSerializer, MenuSerializer, 
    MenuEditSerializer, DishTypeSerializer ,
    DishSerializer, UserShiftsOnlySerializer,
    ListUserSerializer, UpdateUserRoleSerializer,
    UpdateShiftsSerializer, ListShiftsAvailabilitySerializer,
    
    )
from .models import User, Category, Dish, DishType
from rest_framework import generics, permissions
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.permissions import AllowAny
from collections import defaultdict
from django.shortcuts import get_object_or_404
from django.db.models import Count

logger = logging.getLogger(__name__)
        
def get_csrf_token(request):
    csrf_token = get_token(request)
    response = JsonResponse({'token': csrf_token})
    response["Access-Control-Allow-Credentials"] = "true"  # If using CORS
    return response

class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated users to access

    def post(self, request):
        try:
            data = request.data  # DRF automatically parses JSON
            email = data.get('email')
            password = data.get('password')

            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                response = JsonResponse({"message": "Login successful"})
                response.set_cookie("csrftoken", get_token(request), httponly=False, samesite='Lax')
                return response
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
        
        except Exception as e:
            logger.error(f"Login error: {e}")
            return Response({'error': 'An unexpected error occurred'}, status=500)
        
class LogoutView(APIView):
    def post(self, request):
        logout(request)  # Logs out the user by clearing the session
        response = Response({"message": "Logout successful"})
        response.delete_cookie("csrftoken")  # Optional: also delete the CSRF cookie
        return response

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

## Manager Users
class listAllUsers(generics.ListCreateAPIView):
    serializer_class = ListUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
class updateUserRole(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateUserRoleSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    
    def get_object(self):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(User, pk=user_id)
    
class UserRolesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        roles = [{"value": role.value, "label": role.label} for role in User.Role]
        return Response(roles)
    
def countAllUsers(request):
    if request.method == 'GET':
        data = User.objects.values('role').annotate(count=Count('role'))
        return JsonResponse(list(data), safe=False)
    
class shiftsAvailabilityPerUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListShiftsAvailabilitySerializer
        return UpdateShiftsSerializer

## Menus  
class MenuView(generics.ListAPIView):
    queryset = Category.objects.prefetch_related('dishes', 'dish_type').all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        categories = self.get_queryset()
        grouped_menu = defaultdict(lambda: defaultdict(list))

        for category in categories:
            dish_type = category.dish_type.name  # e.g., "Mains"
            extra_dish_type = category.dish_type.extra_dish_type  # e.g., "Chicken", "Beef"

            for dish in category.dishes.all():
                grouped_menu[dish_type][extra_dish_type].append({
                    "id": dish.id,
                    "name": dish.name,
                    "price": str(dish.price),
                    "description": dish.description
                })

        # Convert defaultdict to normal dictionary for JSON response
        response_data = [{"dish_type": dish_type, "extra_dish_types": extra_types} for dish_type, extra_types in grouped_menu.items()]

        return Response(response_data)
    
class GetDishTypesView(generics.ListCreateAPIView):
    queryset = DishType.objects.all()
    serializer_class = DishTypeSerializer
    permission_classes = [permissions.AllowAny]
    
class EditDishTypesView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DishTypeSerializer
    queryset = DishType.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get_object(self):
        obj = get_object_or_404(DishType, pk=self.kwargs["pk"])  # Get by primary key
        self.check_object_permissions(self.request, obj)  # Ensure permissions are enforced
        return obj
    
class ListMenuRawView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = MenuSerializer

class  MenuViewEditor(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuEditSerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get_object(self):
        obj = get_object_or_404(Category, pk=self.kwargs["pk"])  # Get by primary key
        self.check_object_permissions(self.request, obj)  # Ensure permissions are enforced
        return obj
    
class MenuListViewEditor(generics.ListCreateAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    
class DishEditor(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get_object(self):
        obj = get_object_or_404(Dish, pk=self.kwargs["pk"])  # Get by primary key
        self.check_object_permissions(self.request, obj)  # Ensure permissions are enforced
        return obj
    
    
    
@api_view(['GET'])
def check_auth(request):
    if request.user.is_authenticated:
        return Response({"message": "User is authenticated", "user": request.user.email})
    else:
        return Response({"message": "User is not authenticated"}, status=403)

class viewAllUserShiftAvailability(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        users = User.objects.prefetch_related('shift_available').all()
        
        shift_dict = defaultdict(list)  # Stores shifts as keys, and list of users as values
        
        for user in users:
            for shift in user.shift_available.all():
                shift_dict[str(shift)].append({"id": user.id, "name": user.name})  # Store user ID & name
        
        # Convert dictionary to a list of dicts for JSON response
        return [{"shift": shift, "users": sorted(users, key=lambda x: x['name'])} for shift, users in sorted(shift_dict.items())]

    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        return Response(data)
