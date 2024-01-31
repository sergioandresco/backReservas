"""backReservas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apisReserve.views import create_event, get_all_events, create_reserv, register_user, login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-event/', create_event, name='create_event'),
    path('all-events/', get_all_events, name='get_all_events'),
    path('create-reserv/', create_reserv, name='create_reserv'),
    path('create-user/', register_user, name='create_user'),
    path('login/', login_user, name='login'),
]
