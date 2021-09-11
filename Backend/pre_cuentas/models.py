from django.db import models
from django.db.models.deletion import CASCADE

class Client(models.Model):
    document_id = models.AutoField(primary_key=True)
    document_type = models.CharField(max_length=1)                                  # Faltan opciones
    document_number = models.PositiveIntegerField(max_length=10)                    # Faltan opciones
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField(max_length=500)
    state = models.CharField(max_length=1)                                          # Faltan opciones
    def __str__(self):
        return self.document_id
    class Meta:  
        db_table = 'Client'
        constraints = [
            models.UniqueConstraint(fields=['document_type', 'document_number'], name='unique_document')
        ]

class ForeignTransfer(models.Model):
    transfer_abroad = models.CharField(max_length=1)
    origin = models.CharField(max_length=1, blank=True, null=True)
    destiny = models.CharField(max_length=1, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:  
        db_table = 'ForeignTransfer'

class State(models.Model):
    name = models.CharField(max_length=255, unique=True)
    state = models.CharField(max_length=1)                                          # Faltan opciones
    def __str__(self):
        return self.name
    class Meta:  
        db_table = 'State'

class Municipality(models.Model):
    name = models.CharField(max_length=255, unique=True)
    state_code = models.ForeignKey(State, on_delete= models.CASCADE)
    state = models.CharField(max_length=1)                                          # Faltan opciones
    def __str__(self):
        return self.name
    class Meta:  
        db_table = 'Municipality'

class Office(models.Model):
    name = models.CharField(max_length=255, unique=True)
    municipality_code = models.ForeignKey(Municipality, on_delete= models.CASCADE)
    address = models.TextField(max_length=500)
    state = models.CharField(max_length=1)                                          # Faltan opciones
    def __str__(self):
        return self.name
    class Meta:  
        db_table = 'Office'

class Request(models.Model):
    code = models.AutoField(primery_key=True)
    client_document_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    office_code = models.ForeignKey(Office, on_delete=models.CASCADE)
    foreign_transfer_code = models.ForeignKey(Office, on_delete=models.PROTECT)
    account_type = models.CharField(max_length=1)                                   # Faltan opciones
    reason = models.CharField(max_length=1)                                         # Faltan opciones
    expiration_date = models.DateField(auto_now =False, auto_now_add=False)
    date_issue = models.DateField(auto_now =False, auto_now_add=True)
    account_usage = models.CharField(max_length=1)
    estimated_amount_mobilization = models.CharField(max_length=1)                  # Faltan opciones
    average_monthly_transaction = models.CharField(max_length=1)                    # Faltan opciones
    background_source = models.CharField(max_length=1)                              # Faltan opciones
    background_destination = models.CharField(max_length=1)                         # Faltan opciones
    state = models.CharField(max_length=1)                                          # Faltan opciones
    def __str__(self):
        return self.code
    class Meta:  
        db_table = 'Request'

