from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import ClockInOut
from shifts.models import Shift
from .serializers import ClockInOutSummarySerializer
from django.utils import timezone


class ClockInAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        shift_id = request.data.get('shift_id')
        
        if not shift_id:
            return Response({'error': 'Shift ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            shift = Shift.objects.get(id=shift_id)
        except Shift.DoesNotExist:
            return Response({'error': 'Shift not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        today = timezone.now().date()
        clock_record, created = ClockInOut.objects.get_or_create(
            user=user,
            shift=shift,
            date=today
        )

        if clock_record.clock_in_time:
            return Response({'error': 'Already clocked in.'}, status=status.HTTP_400_BAD_REQUEST)
        
        clock_record.clock_in()
        return Response({
            'message': 'Clocked in successfully.',
            'clock_in_time': clock_record.clock_in_time
        }, status=status.HTTP_200_OK)


class ClockOutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        shift_id = request.data.get('shift_id')
        
        if not shift_id:
            return Response({'error': 'Shift ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            shift = Shift.objects.get(id=shift_id)
        except Shift.DoesNotExist:
            return Response({'error': 'Shift not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        today = timezone.now().date()
        try:
            clock_record = ClockInOut.objects.get(user=user, shift=shift, date=today)
        except ClockInOut.DoesNotExist:
            return Response({'error': 'You have not clocked in yet.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if clock_record.clock_out_time:
            return Response({'error': 'Already clocked out.'}, status=status.HTTP_400_BAD_REQUEST)
        
        clock_record.clock_out()
        return Response({
            'message': 'Clocked out successfully.',
            'clock_out_time': clock_record.clock_out_time
        }, status=status.HTTP_200_OK)



class UserClockedShiftSummaryAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        clock_records = ClockInOut.objects.filter(user=request.user).order_by('-date')
        serializer = ClockInOutSummarySerializer(clock_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ClockStatusAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        shift_id = request.query_params.get('shift_id')
        
        if not shift_id:
            return Response({'error': 'Shift ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            shift = Shift.objects.get(id=shift_id)
        except Shift.DoesNotExist:
            return Response({'error': 'Shift not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        today = timezone.now().date()
        try:
            clock_record = ClockInOut.objects.get(user=request.user, shift=shift, date=today)
            data = {
                'clock_in_time': clock_record.clock_in_time,
                'clock_out_time': clock_record.clock_out_time,
                'is_completed': clock_record.is_completed
            }
        except ClockInOut.DoesNotExist:
            data = {
                'clock_in_time': None,
                'clock_out_time': None,
                'is_completed': False
            }
        
        return Response(data, status=status.HTTP_200_OK)
