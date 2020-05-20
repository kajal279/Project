from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from testapp.serializers import Ride_BookSerializer
from testapp.models import Ride_Book
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

class RideListAPIView(APIView):
     def get(self,request,format=None):
         qs=Ride_Book.objects.all()
         serializer=Ride_BookSerializer(qs, many=True)
         return Response(serializer.data)




