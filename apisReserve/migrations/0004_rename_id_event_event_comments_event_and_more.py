# Generated by Django 4.2.9 on 2024-01-29 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apisReserve', '0003_rename_number_of_places_reserv_events_number_of_places_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_comments',
            old_name='id_event',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='event_comments',
            old_name='id_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='reservs',
            old_name='id_event',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='reservs',
            old_name='id_user',
            new_name='user',
        ),
    ]
