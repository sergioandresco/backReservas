from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Definir las clases Event y Place primero
class Events(models.Model):
    name = models.CharField(max_length=450, verbose_name="Name_Event")
    description = models.CharField(max_length=600, verbose_name="Description_Event")
    date_event = models.DateField()
    number_of_places = models.IntegerField(verbose_name="Number_of_places", default=0, help_text="Total number of available seats")
    number_of_places_available = models.IntegerField(verbose_name="Number_of_places_available", default=0, help_text="Number of seats currently reserved")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of Create")
    modified = models.DateTimeField(auto_now_add=True, verbose_name="Date of Modified")
    
# Luego definir las clases que hacen referencia a Places y Events
class Reservs(models.Model):
    STATE_CHOICES = (
        ('activ', 'Active'),
        ('canceled', 'Canceled'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    reservation_date = models.DateField()
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='activ', verbose_name="State")
    places_reserv = models.IntegerField(verbose_name="Number_of_places_reserv", default=0, help_text="Number of places reserv")
    event = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name="Event")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of Create")
    modified = models.DateTimeField(auto_now_add=True, verbose_name="Date of Modified")

@receiver(post_save, sender=Reservs, dispatch_uid="update_places")
def update_places(sender, instance, **kwargs):
    
    event = Events.objects.get(id=instance.event.id)
    event.number_of_places_available = event.number_of_places - instance.places_reserv
    event.save()
    
class Event_comments(models.Model):
    CALIFICATION_CHOICES = [(i, str(i)) for i in range(1, 11)]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", null=True, default=None)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name="Event", null=True, default=None)
    comment_description = models.CharField(max_length=600, verbose_name="Description_Comment")
    event_calification = models.IntegerField(choices=CALIFICATION_CHOICES, verbose_name="Event Calification")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of Create")
    modified = models.DateTimeField(auto_now=True, verbose_name="Date of Modified")
