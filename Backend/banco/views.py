from os import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def landingPage(request):
    return render(request, 'pages/LandingPage.html')

def login_view(request):
    """Login view."""
    if request.user.is_authenticated:
        return redirect('home_user')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home_user')
            else:
                return render(request, 'pages/Login.html', {'error': 'Invalid username and password'})
    return render(request, 'pages/Login.html')
  
@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')