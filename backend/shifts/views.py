from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import Shift, ShiftAvailability, Rota
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import( ShiftSerializer, DaySerializer,
                         HourSerializer, ShiftTypeSerializer, 
                         ShiftAvailSerializer, 
                         ShiftAvailUpdateSerializer,
                         RotaSerializer)
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

## Shift AVAIl
class createUpdateShiftsAvailability(generics.ListCreateAPIView):
    queryset = ShiftAvailability.objects.all()
    permission_class = [IsAuthenticated]       
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ShiftAvailSerializer     
        return ShiftAvailUpdateSerializer
    
class deleteShiftAvailById(generics.RetrieveDestroyAPIView):
    queryset = ShiftAvailability.objects.all()
    serializer_class = ShiftAvailUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        id = self.kwargs['id']
        return ShiftAvailability.objects.get(pk=id)
    
class DeleteShiftAll(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        # Find shift availability not used in any rota
        unassigned_shifts = ShiftAvailability.objects.filter(rota__isnull=True)
        deleted_count, _ = unassigned_shifts.delete()

        return Response(
            {"message": f"Deleted {deleted_count} unassigned shift records. Historical rotas preserved."},
            status=status.HTTP_200_OK
        )


## Rota
class createOrGetRota(generics.ListCreateAPIView):
    queryset = Rota.objects.all()
    serializer_class = RotaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
## Shift 
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