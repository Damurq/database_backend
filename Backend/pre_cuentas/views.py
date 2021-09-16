from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
  
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
def homeUser(request):
    return render(request, 'HomeUser.html')

#@login_required
def messageSC(request):
    return render(request, 'components/MessageSC.html')

@login_required
def clientDataSC(request):
    client = request.user.client
    if request.method == 'POST':
        form = ClientForm(request.POST)
        form.is_valid()
        data = form.cleaned_data
        document_type = data['document_type']
        document_number = data['document_number']
        try:
            if client == Client.objects.get(document_type=document_type,document_number=document_number):            
                return redirect("Form1SC")
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

#@login_required
def form1SC(request):
    form2= ForeignTransferForm()
    form = RequestForm()
    if request.method == 'POST':
        pass
    else:
        form = RequestForm()
    return render(
        request=request,
        template_name='components/Form1SC.html',
        context={
            'form': form,
            "form2":form2
        }
    )
    
#@login_required
def form2SC(request):
    return render(request, 'components/Form2SC.html')

def seeQuote(request):
    return render(request, 'components/SeeQuote.html')

def visualize(request):
    return render(request, 'components/Visualize.html')