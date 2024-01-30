from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Events
from .serializers import EventSerializer, EventList

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