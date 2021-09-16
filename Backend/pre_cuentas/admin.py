from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    pass

class ForeignTransferAdmin(admin.ModelAdmin):
    pass


class StateAdmin(admin.ModelAdmin):
    pass


class MunicipalityAdmin(admin.ModelAdmin):
    pass


class OfficeAdmin(admin.ModelAdmin):
    pass


class RequestAdmin(admin.ModelAdmin):    
    pass


admin.site.register(Client, ClientAdmin)
admin.site.register(ForeignTransfer, ForeignTransferAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Request, RequestAdmin)
