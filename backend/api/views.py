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
from .serializers import LoginSerializer, UserSerializer
from .models import User
from rest_framework import generics, permissions
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.permissions import AllowAny


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
    
@api_view(['GET'])
def check_auth(request):
    if request.user.is_authenticated:
        return Response({"message": "User is authenticated", "user": request.user.email})
    else:
        return Response({"message": "User is not authenticated"}, status=403)
