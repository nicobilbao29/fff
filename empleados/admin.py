from django.contrib import admin
from .models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'departamento', 'fecha_contratacion', 'sueldo')  # Campos que se mostrarán en la tabla
    list_filter = ('departamento',)  # Agrega un filtro por departamento
    search_fields = ('nombre', 'apellido', 'email')  # Permite buscar por nombre, apellido y email
    ordering = ('apellido',)  # Ordena por apellido de forma ascendente


admin.site.register(Empleado, EmpleadoAdmin)