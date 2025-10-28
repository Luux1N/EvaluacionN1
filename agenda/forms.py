from django import forms
from .models import Contacto
import re

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto # nombre del modelo
        fields = ['nombre', 'telefono', 'correo', 'direccion'] # campos del formulario

    

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono') # valida telefono chileno
        if not re.match(r"^\+569\d{8}$", telefono): # formato +569 y 8 digitos
            raise forms.ValidationError("El teléfono debe tener formato +569 y 8 dígitos (ej: +56912345678).") # error si no cumple
        return telefono