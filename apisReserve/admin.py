from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User,
    Events,
    Reservs,
    Event_comments,
)

# Register your models here.

admin.site.register(Events)
admin.site.register(Reservs)
admin.site.register(Event_comments)
