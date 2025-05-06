from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from .models import FinanceReport
from .serializers import ListFinanceSerializer, FinanceReportSerializer

class updateFinanceReport(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            FinanceReport.updateFinancialReport()
            return Response({"message": "Success"})
        
        except Exception as e:
            return Response({"Error": str(e)}, status=500)
        
class getFinanceList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFinanceSerializer
    queryset = FinanceReport.objects.all()
    
class FinanceReportChartAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # or AllowAny if public

    def get(self, request, *args, **kwargs):
        reports = FinanceReport.objects.all().order_by('date')
        serializer = FinanceReportSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
