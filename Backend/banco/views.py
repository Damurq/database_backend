from os import name
from django.http import HttpResponse
from django.shortcuts import redirect, render

def Login(request):
    return render(request, 'pages/Login.html')

def homeUser(request):
    return render(request, 'pages/homeUser.html')

def HomeUser(request):
    return render(request, 'HomeUser.html')

def MessageSC(request):
    return render(request, 'components/MessageSC.html')

def ClientDataSC(request):
    return render(request, 'components/ClientDataSC.html')

def Form1SC(request):
    return render(request, 'components/Form1SC.html')

def Form2SC(request):
    return render(request, 'components/Form2SC.html')

def SeeQuote(request):
    return render(request, 'components/SeeQuote.html')

def Visualize(request):
    return render(request, 'components/Visualize.html')


