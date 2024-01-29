from django.db import models

# Definir las clases Event y Place primero
class Events(models.Model):
    name = models.CharField(max_length=450, verbose_name="Name_Event")
    description = models.CharField(max_length=600, verbose_name="Description_Event")
    id_place = models.ForeignKey('Places', on_delete=models.CASCADE)
    date_event = models.DateField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of Create")
    

class Places(models.Model):
    name = models.CharField(max_length=450, verbose_name="Name_Places")
    locations_available = models.IntegerField(verbose_name="Locations Available")
    address = models.CharField(max_length=450, verbose_name="Address")
    telphone = models.CharField(max_length=250, verbose_name="Telphone")
    id_gestion_of_reserv = models.ForeignKey('Gestion_of_reservs', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of Create")


# Luego definir las clases que hacen referencia a Places y Events
class Gestion_of_reservs(models.Model):
    STATE_CHOICES = (
        ('activ', 'Active'),
        ('canceled', 'Canceled'),
    )
    
    name_of_the_person_booking = models.CharField(max_length=450, verbose_name="Name_Person")
    reservation_date = models.DateField()
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='activ', verbose_name="State")
    id_place = models.ForeignKey(Places, on_delete=models.CASCADE)
    id_event = models.ForeignKey(Events, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of Create")

class Event_comments(models.Model):
    CALIFICATION_CHOICES = [(i, str(i)) for i in range(1, 11)]
    
    comment_description = models.CharField(max_length=600, verbose_name="Description_Comment")
    event_calification = models.IntegerField(choices=CALIFICATION_CHOICES, verbose_name="Event Calification")
    id_gestion_of_reserv = models.ForeignKey(Gestion_of_reservs, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of Create")
