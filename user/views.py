from django.contrib.auth import login, logout

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import RegistrationSerializer, LoginSerializer
from .utils import JWT


class Registration(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"registured successfully","data":serializer.data,"status":201})


class Login(APIView):
    def post(self, request):
        try:

            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            login(request, serializer.context.get("user"))
            user = serializer.context.get("user")
            token = JWT().encode(data={"user_id": user.id})
            return Response({"message": "Login Successfully", "token":token, "status": 201})

        except Exception as e:
            print(e)
            return Response({"message": str(e)}, status=400)

class Logout(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"Message": "Logout Successfully", "status": 200})
        return Response({"Message": "User already logout"})