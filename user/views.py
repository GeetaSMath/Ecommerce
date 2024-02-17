from django.contrib.auth import login
from django.shortcuts import render

# Create your views here.
#registration class based api
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import RegistrationSerializer, LoginSerializer


class Registration(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"registured successfully","data":serializer.data,"status":201})

class Login(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        login(request,serializer.context.get('user'))
        return Response({"message":"login successfullu"})

