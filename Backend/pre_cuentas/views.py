from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from datetime                           import datetime, timedelta, date

def check_availability(limit):
    date_ = None
    for i in range(1,31):
        next_day = date.today() + timedelta(days=i)
        if limit > Request.objects.filter(expiration_date=next_day).count():
            date_ = next_day
            break
    return date_

@login_required
def home_user(request):
    """Loads the start menu of the user panel

    Args:
        request (HttpRequest): object HttpRequest

    Returns:
        HttpResponse: template home_user
    """
    client = request.user.client
    context ={"user":client}
    return render(request, 'pages/home_user.html',context)

@login_required
def request_message(request):
    """Displays a warning message when creating a 
    request to open an account

    Args:
        request (HttpRequest): object HttpRequest

    Returns:
        HttpResponse: template request_message
    """
    client = request.user.client
    context ={"user":client}
    return render(request, 'pages/request_message.html',context)

@login_required
def verification_client(request):
    """View that loads a verification form to validate the 
    client through their identity document

    Args:
        request (HttpRequest): object HttpRequest

    Returns:
        HttpResponse: template request_message
    """
    client = request.user.client
    if request.method == 'POST':
        try:
            form = ClientForm(request.POST)
            form.is_valid()
            data = form.cleaned_data
            document_type = data['document_type']
            document_number = data['document_number']
            if client == Client.objects.get(document_type=document_type,document_number=document_number):            
                return redirect("choice_state")
        except Exception as e:
            return render(request, 'pages/verification_client.html', {'error': 'El documento que ingreso es invalido','form': form,"user":client})
    else:
        form = ClientForm()
    return render(
        request=request,
        template_name='pages/verification_client.html',
        context={
            'form': form, "user":client
        }
    )

@login_required
def choice_state(request):
    """
        View that loads a Form that generates a select with a group of 
        options from all the states 
        and their respective municipalities

    Args:
        request (HttpRequest): object HttpRequest

    Returns:
        HttpResponse: template request_message
    """
    client = request.user.client
    form_state = MunicipalityForm()
    if request.method == 'POST':
        id_municipality=request.POST['municipality']
        return redirect('Form1SC', municipality=int(id_municipality))
    else:
        form_state = MunicipalityForm()
    return render(
        request=request,
        template_name='pages/choice_state.html',
        context={
            'form': form_state, "user":client
        }
    )

@login_required
def create_request(request,municipality):
    client = request.user.client
    #municipality_id = Municipality.objects.get(id=municipality)
    if request.method == 'POST':
        form_office = OfficeForm(request.POST)
        form_request = RequestForm(request.POST)
        if form_office.is_valid() and form_request.is_valid():
            data = form_request.cleaned_data
            try:
                office = Office.objects.get(id=request.POST['office'])
            except Exception as e:
                print("exception")
                print(e)
                return render(request, 'pages/create_request.html', {'error': 'No hay citas disponibles para esta oficina',
                    'form': form_office,
                    'form2': form_request,
                    "user":client
                })
            print("1------------------------------")
            print(dir(office))
            print(office.request_limit_day)
            print("1------------------------------")
            print(check_availability(office.request_limit_day))    
            if check_availability(office.request_limit_day):
                data2 = form_office.cleaned_data
                print("1------------------------------")
                print(data)
                print("1------------------------------")
                a = request.POST['office']
                print("2------------------------------")
                print(a)
                print("2------------------------------")
                print("3------------------------------")
                print(data2)
                print("3------------------------------")
                b = request.POST['average_monthly_transaction']
                print("4------------------------------")
                print(b)
                print("4------------------------------")
                r = Request.objects.create(
                    client_document_id = request.user.client,
                    office_code = office,
                    account_type = data['account_type'] ,                      
                    reason = data['reason'],                                        
                    expiration_date = check_availability(office.request_limit_day),
                    account_usage = data['account_usage'],
                    estimated_amount_mobilization = data['estimated_amount_mobilization'],                 
                    average_monthly_transaction = data['average_monthly_transaction'],   
                    transfer_origin = data['transfer_origin'],
                    transfer_destiny = data['transfer_destiny'],                 
                )

                r.save()
                redirect("home_user")
            else:
                print("else")

                return render(request, 'pages/create_request.html', {'error': 'No hay citas disponibles para esta oficina',
                    'form': form_office,
                    'form2': form_request, 
                    "user":client
                })
            
        else:
            return render(request, 'pages/create_request.html', {'error': 'Invalid document',
            'form': form_office,
            'form2': form_request,
            "user":client
        })
    else:
        form_office = OfficeForm(municipality_id=municipality)
        form_request = RequestForm()
    return render(
        request=request,
        template_name='pages/create_request.html',
        context={
            'form': form_office,
            'form2': form_request,
            "user":client
        }
    )

    
#@login_required
def form2SC(request):
    return render(request, 'components/Form2SC.html')

def seeQuote(request):
    client = request.user.client

    consultQuote = Request.objects.select_related('office_code').filter(client_document_id = client)

    return render(request, 'components/SeeQuote.html',{'consultQuote' : consultQuote} )

def visualize(request):
    client = request.user.client

    consultVoucher = Request.objects.select_related('client_document_id', 'office_code').filter(client_document_id = client)

    return render(request, 'components/Visualize.html', {'consultVoucher' : consultVoucher} )