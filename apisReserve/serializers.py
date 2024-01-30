from rest_framework import serializers
from .models import Events, Reservs

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['name', 'description', 'date_event', 'number_of_places']


class EventList(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id','name', 'description', 'date_event', 'number_of_places', 'number_of_places_available']
        
        
class ReservSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservs
        fields = ['places_reserv', 'event', 'user']