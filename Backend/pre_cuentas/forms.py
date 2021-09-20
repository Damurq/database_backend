from .models import *
from django.forms import ModelForm, Form
from django import forms
from .fields import GroupedModelChoiceField
from django.contrib.auth.models import User

class MunicipalityForm(forms.ModelForm):
    """
        Form that generates a select with a group of options from all the states 
        and their respective municipalities
    """
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
        labels = {
				'municipality': 'Municipio',
		}

class ClientForm(ModelForm):
    """
        Class that generates a verification form to validate the client through his 
        identity document
    """
    class Meta:
        model = Client
        labels = {
				'document_type': 'Tipo de documento',
				'document_number': 'Número de documento',
		}
        fields = ['document_type', 'document_number']

class OfficeForm(Form):
    """
        class that generates a select with all offices

    Args:
        Form ([int:id_municipio]): If it is instantiated with the id of a municipality,
        it shows only the offices of that municipality
    """
    office = forms.ModelChoiceField(queryset= Office.objects.filter(state="A"))
    def __init__(self, *args, **kwargs):
        municipality_id = kwargs.pop('municipality_id', None)
        super(OfficeForm, self).__init__(*args, **kwargs)
        if municipality_id:
            self.fields['office'].queryset = Office.objects.exclude(municipality_code=None).filter(municipality_code=municipality_id)
    class Meta:
        labels = {
            'office': 'Oficina',
		}

class RequestForm(ModelForm):
    """
        Generate a form to register requests
    """
    class Meta:
        model = Request
        labels = {
				'account_type': 'Tipo de cuenta',
				'reason': 'Razón para abrir la cuenta',
                'account_usage': 'Uso de la cuenta',
                'estimated_amount_mobilization': 'Monto estimado de movilización',
                'average_monthly_transaction': 'Promedio de transacciones mensuales',
                'transfer_origin': 'País del que suele enviar dinero',
                'transfer_destiny': 'País de destino',
		}
        fields = ['account_type', 'reason', 'account_usage', 'estimated_amount_mobilization',
                'average_monthly_transaction',
                'transfer_origin', 'transfer_destiny']

class UserForm(ModelForm):
    """
        Generate a form to register users
    """
    class Meta:
        model = User
        labels = {
				'username': 'Nombre de usuario',
				'password': 'Contraseña',
		}
        fields = ['username', 'password']

class ClientForm(ModelForm):
    """
        Generate a form to register clients
    """
    class Meta:
        model = Client
        labels = {
				'document_type': 'Tipo de documento',
				'document_number': 'Número de documento',
                'first_name': 'Nombre',
                'last_name': 'Apellido',
                'address': 'Dirección',
		}
        fields = ['document_type', 'document_number', 'first_name',
                'last_name', 'address']