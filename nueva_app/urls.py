# nueva_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),  # Ruta para el menú principal
    path('registro_gastos/', views.registrar_gastos, name='registro_gastos'),  # Ruta para registrar gastos
]
