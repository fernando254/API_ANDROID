from django.db import models

# Create your models here.


class Usuario(models.Model):
    rut = models.CharField(max_length=11)
    nombre_completo = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=12)
    

    def __str__(self):
        return self.nombre_completo