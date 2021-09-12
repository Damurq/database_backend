from os import name
from django.http import HttpResponse
from django.shortcuts import redirect, render


def HomeUser(request):
    return render(request, 'pages/homeUser.html')
