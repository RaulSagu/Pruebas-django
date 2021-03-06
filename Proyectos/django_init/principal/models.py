from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=120)
    direccion = models.CharField(max_length=150)
    correo = models.EmailField(max_length=100)
