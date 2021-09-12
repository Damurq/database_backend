from os import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def homeUser(request):
    return render(request, 'pages/homeUser.html')

def login(request):
    return render(request,'pages/login.html')
    