from django.db import models

# Create your models here.
from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    departamento = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Agregamos la columna sueldo
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
