from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gasto  # Asegúrate de que tienes un modelo Gasto definido

def menu(request):
    return render(request, 'nueva_app/menu.html')

def registrar_gastos(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        fecha = request.POST.get('fecha')
        # Crea una nueva instancia de Gasto y guárdala
        gasto = Gasto(descripcion=descripcion, monto=monto, fecha=fecha)
        gasto.save()
        return redirect('menu')  # Redirige a la vista del menú después de guardar

    return render(request, 'nueva_app/registro_gastos.html')  # Renderiza la plantilla de registro de gastos
