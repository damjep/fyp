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
from .serializers import LoginSerializer


logger = logging.getLogger(__name__)


def login_view(request) -> JsonResponse:
    if request.method == 'POST':
        try:
            data: Dict[str, Any] = json.loads(request.body)
            email: str = data.get('email')
            password: str = data.get('password')

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                
                return JsonResponse({'message': 'Login successful'})
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)
        except Exception as e:
            logger.error(f"Login error: {e}")
            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)
        
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