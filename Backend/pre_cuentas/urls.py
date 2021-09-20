from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_user, name = 'home_user'),
    path('solicitar_cita/', request_message, name = 'MessageSC'),
    path('solicitar_cita/verification', verification_client, name = 'ClientDataSC'),
    path('solicitar_cita/choice_state', choice_state, name = 'choice_state'),
    path('solicitar_cita/request/<int:municipality>/', create_request, name = 'Form1SC'),
    path('ver_cita/', see_quote, name='SeeQuote'),
    path('ver_cita/visualizar/<str:code_request>/', visualize_quote, name='VisualizeQuote'),
    path('reporte/<str:code>/', reportPDF.as_view(), name="report"),
]

