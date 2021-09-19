from .models import *
from django.forms import ModelForm, Form
from django import forms


class ClientForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = Client
        fields = ['document_type', 'document_number']


# class StateForm(ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = State
#         fields = ['name']


# class MunicipalityForm(ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = Municipality
#         fields = ['name', 'state_code']


# class OfficeForm(ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = Office
#         fields = ['name', 'municipality_code', 'address']

class OfficeForm(forms.Form):
    state = forms.ModelChoiceField(
        queryset = State.objects.all()
    )
    municipality = forms.ModelChoiceField(
        queryset = Municipality.objects.all()
    )
    office = forms.ModelChoiceField(
        queryset = Office.objects.all()
    )

class RequestForm(ModelForm):
    state = forms.ModelChoiceField(
        queryset = State.objects.all()
    )
    municipality = forms.ModelChoiceField(
        queryset = Municipality.objects.all()
    )
    office = forms.ModelChoiceField(
        queryset = Office.objects.all()
    )

    # specify the name of model to use
    class Meta:
        model = Request
        fields = ["office","municipality","state",'account_type', 'reason', 'expiration_date', 'account_usage', 'estimated_amount_mobilization', 'average_monthly_transaction',
                  'transfer_origin', 'transfer_destiny']
