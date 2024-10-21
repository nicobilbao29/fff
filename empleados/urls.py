from django.urls import path
from .views import agregar_empleado, listar_empleados, index, obtener_datos_excel, editar_empleado, eliminar_empleado

urlpatterns = [
    path('', index, name='index'),  # Ruta para el index
    path('empleados/', listar_empleados, name='listar_empleados'),
    path('agregar_empleado/', agregar_empleado, name='agregar_empleado'),
    path('editar_empleado/<int:id>/', editar_empleado, name='editar_empleado'),  # Ruta para editar empleado
    path('eliminar_empleado/<int:id>/', eliminar_empleado, name='eliminar_empleado'),  # Ruta para eliminar empleado
    path('obtener_datos_excel/', obtener_datos_excel, name='obtener_datos_excel'),  # Nueva ruta para obtener datos
]
