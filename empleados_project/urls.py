"""
URL configuration for empleados_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# empleados_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from empleados.views import index  # Importamos la vista index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleados/', include('empleados.urls')),  # Incluye todas las rutas de empleados
    path('', RedirectView.as_view(url='/empleados/', permanent=False)),  # Redirige la raíz a empleados
    path('nueva_app/', include('nueva_app.urls')),
]

