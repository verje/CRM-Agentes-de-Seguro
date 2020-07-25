"""ensurance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from app_ensurance import views, forms
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', login_required(TemplateView.as_view(template_name="PlanForm.html"))),
    path('', views.IndexView.as_view(), name="indexview"),
    path('planes/', login_required(views.PlanesView.as_view()), name="planesview"),
    path('crear_cliente/', login_required(forms.ManageFormCrearCliente),
         name='crear_cliente'),
    path('planilla/', login_required(forms.ManagePlanilla)),
    path('listado_planillas/', views.ListaPlanillas.as_view(
        template_name="vistas/planillas_view.html"), name='planillas'),
    path('login/', auth_views.LoginView.as_view(template_name='formlogin.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', login_required(views.ProfileView.as_view()), name="profile"),

    path('listado_clientes/', views.ListaClientes.as_view(
        template_name="vistas/clientes_view.html"), name='clientes'),
    # path('clientes_detalle/<int:pk>', ClientesDetalle.as_view(template_name = "vistas/detalles.html"), name='detalle_clientes'),
    # path('clientes_editar/<int:pk>', ClientesActualizar.as_view(template_name = "vistas/actualizar.html"), name='modificar_clientes'),
    path('listado_clientes/eliminar/<int:pk>',
         views.ClientesEliminar.as_view(), name='eliminar'),
    path('listado_planillas/eliminar/<int:pk>',
         views.PlanillasEliminar.as_view(), name='eliminar'),

]
