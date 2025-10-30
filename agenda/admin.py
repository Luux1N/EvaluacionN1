from django.contrib import admin
from .models import Contacto
admin.site.site_header = "Agenda de Contactos"
admin.site.index_title = "Panel de Administración de Contactos"

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):

    list_display = ("nombre", "correo", "telefono", "direccion")

    search_fields = ("nombre", "correo", "telefono", "direccion")    
   
    list_per_page = 25
#
    ordering = ("nombre",)
    list_per_page = 25
    autocomplete_fields = () # ej.: ("categoria",) si existiera FK grande