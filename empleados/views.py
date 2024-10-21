from django.shortcuts import render, redirect
from .models import Empleado
from .forms import EmpleadoForm
from django.shortcuts import get_object_or_404

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/agregar_empleado.html', {'form': form})



def editar_empleado(request, id):  # Cambia 'empleado_id' por 'id'
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/editar_empleado.html', {'form': form})


def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listar_empleados')
    return render(request, 'empleados/eliminar_empleado.html', {'empleado': empleado})



from django.shortcuts import render
from .models import Empleado

def listar_empleados(request):
    empleados = Empleado.objects.all()  # Obtener todos los empleados
    return render(request, 'empleados/listar_empleados.html', {'empleados': empleados})


# Nueva vista para el index
def index(request):
    return render(request, 'empleados/index.html')





##################################################################################################################################################import pandas as pd
from django.http import JsonResponse

def obtener_datos_excel(request):
    # Cambia 'ruta/a/tu/archivo.xlsx' a la ruta de tu archivo Excel
    df = pd.read_excel('D:\FLASK\django_menu\ventas_ejemplo.xlsx')
    
    # Supongamos que tienes columnas "Mes" y "Ventas" en tu archivo Excel
    data = {
        "meses": df["Mes"].tolist(),
        "ventas": df["Ventas"].tolist(),
    }
    
    return JsonResponse(data)



