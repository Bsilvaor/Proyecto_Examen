from django.db import models

# Create your models here.
class Socio(models.Model):
    dni = models.CharField(primary_key=True, max_length=10)  # DNI lo pongo como clave primaria
    numerosocio = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
