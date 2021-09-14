from django.shortcuts import render

from .forms import *
  
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