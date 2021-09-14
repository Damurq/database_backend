from .models import *
from django.forms import ModelForm


class ClientForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = Client
        fields = ['document_type', 'document_number']


class ForeignTransferForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = ForeignTransfer
        fields = ['transfer_abroad', 'origin', 'destiny']


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


class RequestForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = Request
        fields = ['office_code', 'foreign_transfer_code', 'account_type', 'reason', 'expiration_date', 'account_usage', 'estimated_amount_mobilization', 'average_monthly_transaction',
                  'background_source', 'background_destination']
