from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from datetime                          import datetime, timedelta
from django.utils.timezone import now

def check_availability(limit):
    date = None
    for i in range(1,31):
        next_day = datetime.now().date() + timedelta(days=i)
        if limit > Request.objects.filter(expiration_date=next_day).count():
            date = next_day
            break
    return date

def client_view(request):
    context ={}
    # create object of form
    form = ClientForm(request.POST)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form']= form
    return render(request, "pages/cliente.html", context)

@login_required
def home_user(request):
    return render(request, 'HomeUser.html')

@login_required
def request_message(request):
    return render(request, 'components/MessageSC.html')


@login_required
def verification_client(request):
    client = request.user.client
    if request.method == 'POST':
        form = ClientForm(request.POST)
        form.is_valid()
        data = form.cleaned_data
        document_type = data['document_type']
        document_number = data['document_number']
        try:
            if client == Client.objects.get(document_type=document_type,document_number=document_number):            
                return redirect("choice_state")
            else:
                return render(request, 'components/ClientDataSC.html', {'error': 'Invalid document','form': form})
        except ObjectDoesNotExist:
            return render(request, 'components/ClientDataSC.html', {'error': 'Invalid document','form': form})
        except Exception as e:
            return render(request, 'components/ClientDataSC.html', {'error': 'Invalid document','form': form})
    else:
        form = ClientForm()
    return render(
        request=request,
        template_name='components/ClientDataSC.html',
        context={
            'form': form
        }
    )


@login_required
def create_request(request,municipality):
    #municipality_id = Municipality.objects.get(id=municipality)
    if request.method == 'POST':
        form_office = OfficeForm(request.POST)
        form_request = RequestForm(request.POST)
        if form_office.is_valid() and form_request.is_valid():
            data = form_request.cleaned_data
            if check_availability:
                r = Request.objects.create(
                    client_document_id = request.user.client,
                    office_code = request.POST['office'],
                    account_type = data['account_type'] ,                      
                    reason = data['reason'],                                        
                    expiration_date = check_availability,
                    account_usage = data['account_usage'],
                    estimated_amount_mobilization = data['estimated_amount_mobilization'],                 
                    average_monthly_transaction = data['average_monthly_transaction'],   
                    transfer_origin = data['transfer_origin'],
                    transfer_destiny = data['transfer_destiny'],                 
                )
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
                r.save()
                redirect("home_user")
            else:
                return render(request, 'components/ClientDataSC.html', {'error': 'No hay citas disponibles para esta oficina',
                    'form': form_office,
                    'form2': form_request
                })
        else:
            return render(request, 'components/ClientDataSC.html', {'error': 'Invalid document',
            'form': form_office,
            'form2': form_request
        })
    else:
        form_office = OfficeForm(municipality_id=municipality)
        form_request = RequestForm()
    return render(
        request=request,
        template_name='components/Form1SC.html',
        context={
            'form': form_office,
            'form2': form_request
        }
    )

@login_required
def choice_state(request):
    form_state = MunicipalityForm()
    if request.method == 'POST':
        id_municipality=request.POST['municipality']

        return redirect('Form1SC', municipality=int(id_municipality))
    else:
        form_state = MunicipalityForm()
    return render(
        request=request,
        template_name='components/choice_state.html',
        context={
            'form': form_state,
        }
    )

    
#@login_required
def form2SC(request):
    return render(request, 'components/Form2SC.html')

def seeQuote(request):
    return render(request, 'components/SeeQuote.html')

def visualize(request):
    return render(request, 'components/Visualize.html')