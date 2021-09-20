from pre_cuentas.models import Client
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from pre_cuentas.forms import UserForm, ClientForm
from django.db.utils import IntegrityError
from django.contrib.auth.models import User

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


def sign_up_view(request):
    """Login view."""
    form_user = UserForm()
    if request.user.is_authenticated:
        return redirect('home_user')
    else:
        if request.method == 'POST':
            form_user = UserForm(request.POST)
            form_client = ClientForm(request.POST)
            if form_user.is_valid() and form_client.is_valid():
                username = request.POST['username']
                passwd = request.POST['password']
                passwd_confirmation = request.POST['passwd_confirmation']
                if passwd != passwd_confirmation:
                    return render(request, 'pages/sign_up.html', {'error': 'Password confirmation does not match'})
                try:
                    user = User.objects.create_user(username=username, password=passwd)
                except IntegrityError:
                    return render(request, 'pages/sign_up.html', {'error': 'Username is already in user'})
                document_type = request.POST['document_type']
                document_number = request.POST['document_number']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                address = request.POST['address']
                user.email = request.POST['email']
                user.save()
                client = Client.objects.create(user=user,document_type=document_type,document_number=document_number,
                                first_name=first_name, last_name=last_name, address=address
                )
                client.save()
                if user:
                    login(request, user)
                    return redirect('login')
            else:
                return render(request, 'pages/sign_up.html', {'error': 'datos invalidos',
                    'form': form_user,
                    'form2': form_client, 
                })
        else:
            form_user = UserForm()
            form_client = ClientForm()
    return render(
        request=request,
        template_name='pages/sign_up.html',
        context={
            'form': form_user,
            'form2': form_client,
        }
    )