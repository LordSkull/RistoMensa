"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mensa.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('login', login, name='login'),
    path('prenotazione', effettua_prenotazione, name='prenotazione'),
    path('area_dipendente/', area_dipendente, name='area_dipendente'),
    path('next', conferma_prenotazione, name='conferma_prenotazione'),
    path('gestione_menu/', gestione_menu, name='gestione_menu'),
    path('elimina_prenotazione/<int:id>/', elimina_prenotazione, name='elimina_prenotazione'),
    path('home/', index, name='home'),
    path('reset_tavoli/', reset_tavoli_struttura, name='reset_tavoli_struttura'),
    path('reset_tavolo/<int:id_tavolo>/', reset_tavolo_singolo, name='reset_tavolo'),
]

