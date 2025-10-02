from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)  # correo único, no se pueden repetir
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} ({self.correo})"