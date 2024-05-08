from django.db import models

class Persona(models.Model):
    cabeza_hogar = models.BooleanField(default=False)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    tipo_documento = models.CharField(max_length=50)
    numero_identificacion = models.CharField(max_length=100)
