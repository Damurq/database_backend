from .models import *
from django.forms import ModelForm, Form
from django import forms
from .fields import GroupedModelChoiceField

class MunicipalityForm(forms.ModelForm):
    municipality = GroupedModelChoiceField(
        queryset=Municipality.objects.exclude(state_code=None), 
        choices_groupby='state_code'
    )
    def __init__(self, *args, **kwargs):
        state_id = kwargs.pop('state_id', None)
        super(MunicipalityForm, self).__init__(*args, **kwargs)
        if state_id:
            self.fields['municipality'].queryset = Municipality.objects.exclude(state_code=None).filter(state_code=state_id)
    class Meta:
        model = Municipality
        fields = ['municipality']

class ClientForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = Client
        fields = ['document_type', 'document_number']


class StateForm(Form):
    state = forms.ModelChoiceField(
        queryset = State.objects.filter(state="A")
    )
    class Meta:
        fields = ['state']
        labels = {
				'state': 'Estado',
		}

# class MunicipalityForm(Form):
#     municipality = forms.ModelChoiceField(queryset= Municipality.objects.filter(state="A"))
#     def __init__(self, *args, **kwargs):
#         state_id = kwargs.pop('state_id', None)
#         super(MunicipalityForm, self).__init__(*args, **kwargs)
#         if state_id:
#             self.fields['municipality'].queryset = Municipality.objects.filter(state_code=state_id)

class OfficeForm(Form):
    # specify the name of model to use
    office = forms.ModelChoiceField(queryset= Office.objects.filter(state="A"))
    def __init__(self, *args, **kwargs):
        municipality_id = kwargs.pop('municipality_id', None)
        super(OfficeForm, self).__init__(*args, **kwargs)
        if municipality_id:
            self.fields['office'].queryset = Office.objects.exclude(municipality_code=None).filter(municipality_code=municipality_id)

class RequestForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = Request
        fields = ['account_type', 'reason', 'account_usage', 'estimated_amount_mobilization', 'average_monthly_transaction',
                'transfer_origin', 'transfer_destiny']
