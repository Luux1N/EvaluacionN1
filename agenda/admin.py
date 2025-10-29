from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    
    list_display = ("nombre", "correo", "telefono")
    
    search_fields = ("nombre", "correo", "telefono")
   
    list_per_page = 25
#
    ordering = ("nombre",)