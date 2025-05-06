from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from .models import Rating
from rest_framework import generics, permissions
from .serializers import (
    ListSerializer
)


class AverageRatingAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        avg_rating = Rating.objects.aggregate(avg=Avg('rating'))['avg'] or 0
        avg_rating = round(avg_rating, 2)
        return Response({"average_rating": avg_rating}, status=status.HTTP_200_OK)
    
class getCreateRatingList(generics.ListCreateAPIView):
    queryset= Rating.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.AllowAny]