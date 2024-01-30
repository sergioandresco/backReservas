from rest_framework import serializers
from .models import Events

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['name', 'description', 'date_event', 'number_of_places']


class EventList(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['name', 'description', 'date_event', 'number_of_places', 'number_of_places_available']