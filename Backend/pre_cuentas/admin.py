from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)
