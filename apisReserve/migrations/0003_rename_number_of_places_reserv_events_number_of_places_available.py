# Generated by Django 4.2.9 on 2024-01-29 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apisReserve', '0002_reservs_remove_places_id_gestion_of_reserv_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='number_of_places_reserv',
            new_name='number_of_places_available',
        ),
    ]