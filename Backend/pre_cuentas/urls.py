from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', homeUser, name = 'home_user'),
    path('solicitar_cita/', messageSC, name = 'MessageSC'),
    path('solicitar_cita/12', clientDataSC, name = 'ClientDataSC'),
    path('solicitar_cita/12/32', form1SC, name = 'Form1SC'),
    path('solicitar_cita/12/32/27', form2SC, name = 'Form2SC'),
    path('ver_cita/', seeQuote, name='SeeQuote'),
    path('visualizar/', visualize, name='Visualize'),
]

