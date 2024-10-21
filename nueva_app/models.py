from django.db import models

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)  # Campo para la descripción del gasto
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para el monto del gasto
    fecha = models.DateField()  # Campo para la fecha del gasto

    def __str__(self):
        return f"{self.descripcion} - {self.monto} - {self.fecha}"
