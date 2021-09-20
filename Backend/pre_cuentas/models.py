from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    """
    Client.

    """
    DOCUMENT_TYPE = (
        ("V","Venezolano"),
        ("E","Extranjero")
    )
    document_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=1,choices=DOCUMENT_TYPE)                                  # Faltan opciones
    document_number = models.PositiveIntegerField()                    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField(max_length=500)
    state = models.CharField(max_length=1, default='A')                                          # Faltan opciones
    def __str__(self):
        return self.first_name + " "+ self.last_name
    class Meta:  
        db_table = 'Client'
        constraints = [
            models.UniqueConstraint(fields=['document_type', 'document_number'], name='unique_document')
        ]

class State(models.Model):
    name = models.CharField(max_length=255, unique=True)
    state = models.CharField(max_length=1, default='A')                                          # Faltan opciones
    def __str__(self):
        return self.name
    class Meta:  
        db_table = 'State'

class Municipality(models.Model):
    name = models.CharField(max_length=255, unique=True)
    state_code = models.ForeignKey(State, on_delete= models.CASCADE)
    state = models.CharField(max_length=1, default='A')                                          # Faltan opciones
    def __str__(self):
        return self.name
    class Meta:  
        db_table = 'Municipality'

class Office(models.Model):
    name = models.CharField(max_length=255, unique=True)
    municipality_code = models.ForeignKey(Municipality, on_delete= models.CASCADE)
    address = models.TextField(max_length=500)
    request_limit_day = models.SmallIntegerField(default=1)
    state = models.CharField(max_length=1, default='A')                                          # Faltan opciones
    def __str__(self):
        return self.name
    class Meta:  
        db_table = 'Office'

class Request(models.Model):
    ACCOUNT_TYPE = (
        ("CA", "Cuenta de ahorro"),
        ("CC", "Cuenta corriente")
    )
    REASON = (
        ("BS", "Buen servicio y variedad de productos"),
        ("CT", "Cliente tradicional"),
        ("CN", "Cuenta Nomina"),
        ("GFB", "Gestion de Funcionario del banco"),
        ("NN", "Por estar a nivel nacional"),
        ("SPS", "Por la solidez / prestigio / seguridad"),
        ("AI", "Por los altos intereses"),
        ("PRE", "Por los premios"),
        ("PUB", "Publicidad"),
        ("RFA", "Referencia de un familiar / amigo")
    )
    ACCOUNT_USAGE = (
        ("APE", "Ahorro personal"),
        ("AGVP", "Atender gastos varios / personales"),
        ("CCC", "Cancelar cuotas de credito"),
        ("DV", "Deposito de las ventas"),
        ("MFNPF", "Movilizar fondos de nomina / pension / fideicomiso"),
        ("PP", "Pago de proveedores"),
        ("P", "Particular"),
        ("RDA", "Recibir deposito de alquileres"),
        ("RIDP", "Recibir intereses de depositos a plazo")
    )
    ESTIMATED_AMOUNT_MOBILIZATION = (
        ("En0y500", "Entre 0 y 500"),
        ("En100001y100000", "Entre 10.001 y 100.000"),
        ("En2501y10000", "Entre 2.501 y 10.000"),
        ("En501y2500", "Entre 501 y 2.500"),
        ("Ma100001", "Mas de 100.001")
    )
    AVERAGE_MONTHLY_TRANSACTION = (
        ("Ma100", "Mayor que 100"),
        ("Me20", "Menor que 20"),
        ("Ma20Me50", "Mayor que 20 y menor que 50"),
        ("Ma51Me100", "Mayor que 51 y menor que 100")
    )
    COUNTRIES = (
        ("Ven", "Venezuela"),
        ("Col", "Colombia"),
        ("Per", "Peru"),
        ("Chi", "Chile"),
        ("Bra", "Brasil"),
        ("Arg", "Argentina"),
        ("Ecu", "Ecuador")
    )
    code = models.AutoField(primary_key=True)
    client_document_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    office_code = models.ForeignKey(Office, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPE)                                  
    reason = models.CharField(max_length=3,choices=REASON)                                        
    expiration_date = models.DateField(auto_now =False, auto_now_add=False)
    date_issue = models.DateField(auto_now =False, auto_now_add=True)
    account_usage = models.CharField(max_length=5, choices=ACCOUNT_USAGE)
    estimated_amount_mobilization = models.CharField(max_length=15, choices=ESTIMATED_AMOUNT_MOBILIZATION)                  
    average_monthly_transaction = models.CharField(max_length=9, choices=AVERAGE_MONTHLY_TRANSACTION)   
    transfer_origin = models.CharField(max_length=3, choices=COUNTRIES, default="Ven")
    transfer_destiny = models.CharField(max_length=3, choices=COUNTRIES, default="Ven")                 
    state = models.CharField(max_length=1, default='A')                                          # Faltan opciones
    def __str__(self):
        return str(self.code)
    class Meta:  
        db_table = 'Request'

