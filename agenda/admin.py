from django.contrib import admin
from .models import Contacto

@admin.register(Contacto) # muestra modelo en admin
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono') # columnas visibles
    search_fields = ('nombre', 'correo') # campos de busqueda