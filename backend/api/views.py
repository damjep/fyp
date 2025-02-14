from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
import logging
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from typing import Dict, Any
import json
from rest_framework.views import APIView
from .serializers import LoginSerializer, UserSerializer, MenuSerializer, DishSerializer
from .models import User, Category, Dish
from rest_framework import generics, permissions
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.permissions import AllowAny
from collections import defaultdict
from django.shortcuts import get_object_or_404




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

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class MenuView(generics.ListAPIView):
    queryset = Category.objects.order_by('dish_type').all()
    serializer_class = MenuSerializer
    permissions_classes = [permissions.AllowAny]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = self.get_serializer(queryset, many=True).data

        # Group menus by dish_type
        grouped_data = defaultdict(list)
        for item in serialized_data:
            dish_type_name = item["dish_type"]["name"]
            grouped_data[dish_type_name].append(item)

        return Response(grouped_data)

class  MenuViewEditor(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        obj = get_object_or_404(Category, pk=self.kwargs["pk"])  # Get by primary key
        self.check_object_permissions(self.request, obj)  # Ensure permissions are enforced
        return obj
    
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
