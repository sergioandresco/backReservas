# Generated by Django 4.2.9 on 2024-01-31 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apisReserve', '0007_events_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='image',
        ),
    ]
