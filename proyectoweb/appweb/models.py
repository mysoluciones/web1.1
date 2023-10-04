from django.db import models


class Busqueda(models.Model):  # Cambiado "model" a "models"
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()

# para el formulario

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    tipo_servicio = models.CharField(max_length=20, choices=[('Diseño web', 'Diseño web'), ('Redes sociales', 'Redes sociales'), ('Otro', 'Otro')])
    consulta = models.TextField()

    def __str__(self):
        return self.nombre_apellido