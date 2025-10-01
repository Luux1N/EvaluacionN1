from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion']

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if not correo or '@' not in correo:
            raise forms.ValidationError("ingrese un correo valido") # valida @
        return correo