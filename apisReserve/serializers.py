from rest_framework import serializers
from .models import Events, Reservs, User

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['name', 'description', 'date_event', 'number_of_places', 'number_of_places_available']


class EventList(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id','name', 'description', 'date_event', 'number_of_places', 'number_of_places_available']
        
        
class ReservSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservs
        fields = ['places_reserv', 'event', 'user']
       
       
class ReservListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservs
        fields = ['id','state' ,'places_reserv', 'event', 'user'] 
        
class ReservStateUpdateSerializer(serializers.Serializer):
    state = serializers.ChoiceField(choices=Reservs.STATE_CHOICES)

    def update(self, instance, validated_data):
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

