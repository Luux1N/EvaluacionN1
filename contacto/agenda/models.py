from django.db import models
from django.core.validators import EmailValidator

class Contacto(models.Model):
    nombre = models.CharField(max_length=100) # nombre del contacto
    telefono = models.CharField(max_length=20) # telefono
    correo = models.EmailField(validators=[EmailValidator()]) # correo valido
    direccion = models.CharField(max_length=200) # direccion

    def __str__(self):
        return f"{self.nombre} ({self.correo})" # representacion sencilla