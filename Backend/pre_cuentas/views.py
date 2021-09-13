from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

#@login_required
def homeUser(request):
    return render(request, 'HomeUser.html')

def messageSC(request):
    return render(request, 'components/MessageSC.html')

def clientDataSC(request):
    return render(request, 'components/ClientDataSC.html')

def form1SC(request):
    return render(request, 'components/Form1SC.html')

def form2SC(request):
    return render(request, 'components/Form2SC.html')
