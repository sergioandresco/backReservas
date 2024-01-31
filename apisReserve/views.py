from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Events
from .serializers import EventSerializer, EventList, ReservSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt import views as rfs_views
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator


class ProtectedView(APIView):
    permission_classes = (IsAuthenticated,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Create your views here.
@api_view(['POST'])
def create_event(request):
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_all_events(request):
    if request.method == 'GET':
        events = Events.objects.all()
        serializer = EventList(events, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
def create_reserv(request):
    if request.method == 'POST':
        serializer = ReservSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class CustomTokenObtainPairView(rfs_views.TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        User = get_user_model()
        user = User.objects.filter(username=username).first()

        if user is not None:
            if user.is_active == True:
                user = authenticate(username=username, password=password)
                if user:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    return Response(
                        {
                            "error": "null",
                            "data": serializer.validated_data, 
                            "status": status.HTTP_200_OK 
                        }
                    )
                else:
                    return Response(
                        {
                            "error": "Contraseña incorrecta",
                            "data": [],
                            "status":status.HTTP_401_UNAUTHORIZED 
                        }
                    )
            else:
                return Response(
                    {
                        "error": "El usuario se encuentra inactivo",
                        "data": [],
                        "status": status.HTTP_401_UNAUTHORIZED 
                    }
                )
        else:
            return Response(
                {
                    "error": "El usuario no existe",
                    "data": [], 
                    "status": status.HTTP_401_UNAUTHORIZED })
            
            
