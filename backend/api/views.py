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



logger = logging.getLogger(__name__)
        
def get_csrf_token(request) -> JsonResponse:
    token = get_token(request)
    return JsonResponse({'token': token})

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            user = authenticate(request, email=email, password=password)
            
            if user: 
                login(request, user)
                return Response({'message': 'Login successful'}, status=200)
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
            
        else:
            return Response(serializer.errors, status=400)
        
    def get(self, request):
        return get_csrf_token(request)
    
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # Returns only the authenticated user
