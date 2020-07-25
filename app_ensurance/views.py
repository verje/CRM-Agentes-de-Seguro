from django.shortcuts import render
# trae del archive models.py la clas Blog que creamos como modelo de datos
from .models import *
# importamos una utilidad de Django para generar vistas
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse


def logout_view(request):
    logout(request)
    return render(request, '/')


class PlanesView(generic.ListView):
    model = plan
    template_name = "planes.html"
    context_object_name = "plan_Objects"


class IndexView(generic.TemplateView):
    template_name = "index.html"


class ProfileView(generic.TemplateView):
    template_name = "profile.html"


class ListaClientes(generic.ListView):
    model = Clientes


class ListaPlanillas(generic.ListView):
    model = Planilla


class ClientesEliminar(SuccessMessageMixin, DeleteView):
    model = Clientes
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Cliente Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('clientes')


class PlanillasEliminar(SuccessMessageMixin, DeleteView):
    model = Planilla
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Planilla Eliminada Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('planillas')
