from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Shift
from rest_framework.permissions import AllowAny
from .serializers import ShiftSerializer, DaySerializer, HourSerializer, ShiftTypeSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class getOrCreateShifts(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [AllowAny]
    
class UpdateShiftByID(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [AllowAny]
    
    def get_object(self):
        return get_object_or_404(Shift, id=self.kwargs['pk'])
    
class getShiftsDays(APIView):
    serializer_class = DaySerializer
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        days = [{'key': key, 'value': value} for key, value in Shift.Days.choices]
        return Response(days)
    
class getHours(APIView):
    serializer_class = HourSerializer
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        hours = [{'key': key, 'value': value} for key, value in Shift.HOURS]
        return Response(hours)


class getShiftTypes(APIView):
    serializer_class = ShiftTypeSerializer
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        shift_types = [{'key': key, 'value': value} for key, value in Shift.Shift_Type.choices]
        return Response(shift_types)