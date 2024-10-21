from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    fecha_contratacion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    
    
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'email', 'telefono', 'departamento', 'fecha_contratacion', 'sueldo']
