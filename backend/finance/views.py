from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework.response import Response
from .models import FinanceReport
from .serializers import ListFinanceSerializer

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
    
