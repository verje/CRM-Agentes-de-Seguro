from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import plan, Planilla, Clientes


class DateInput(forms.DateInput):
    input_type = 'date'


class ClienteForm(forms.ModelForm):
    # Declaramos una clase Meta donde indicamos el modelo que va a contener el formulario
    class Meta:
        model = Clientes  # Usamos el modelo importado en la linea 4
        # indicamos que vamos a incluir todos los campos del modelo Blog (3 campos)
        fields = '__all__'
        widgets = {
            'fechanacimiento': DateInput(),
        }


class PlanillaForm(forms.ModelForm):
    # Declaramos una clase Meta donde indicamos el modelo que va a contener el formulario
    class Meta:
        model = Planilla  # Usamos el modelo importado en la linea 4
        # indicamos que vamos a incluir todos los campos del modelo Blog (3 campos)
        fields = '__all__'

        widgets = {
            'fechanacimiento': DateInput(),
            'fechainicio': DateInput(),
            'pregunta1': forms.RadioSelect(),
            'pregunta2': forms.RadioSelect(),
            'pregunta3': forms.RadioSelect(),
        }


# Creamos un metodo para manejar el formulario una vez que se haga clic en el Boton Submit. Este metodo será llamado desde el archivo app_urls.py
def ManageFormCrearCliente(request):
    template_name = "crearCliente.html"
    if request.method == 'POST':
        form = ClienteForm(request.POST or None)
        errors = None
        if form.is_valid():  # Se valida que todos los campos se hayan llenado
            form.save()  # Se guardan los datos a la base de datos
            # una vez procesado el Form y guardado los datos, redireccionamos al index
            return HttpResponseRedirect('/listado_clientes/')
        if form.errors:  # Si hay errores en el form; es decir, no se llenan todos los campos
            errors = form.errors  # Guardamos en la variable errors, los errores encontrados
        context = {"form": form, "errors": errors}
        return render(request, template_name, context)
    else:
        form = ClienteForm()
        return render(request, template_name, {'form': form})


def ManagePlanilla(request):  # Creamos un metodo para manejar el formulario una vez que se haga clic en el Boton Submit. Este metodo será llamado desde el archivo app_urls.py
    template_name = "planilla.html"
    if request.method == 'POST':
        form = PlanillaForm(request.POST or None)
        errors = None
        if form.is_valid():  # Se valida que todos los campos se hayan llenado
            form.save()  # Se guardan los datos a la base de datos
            # una vez procesado el Form y guardado los datos, redireccionamos al index
            return HttpResponseRedirect("/listado_planillas/")
        if form.errors:  # Si hay errores en el form; es decir, no se llenan todos los campos
            errors = form.errors  # Guardamos en la variable errors, los errores encontrados
            print(errors)
        context = {"form": form, "errors": errors}
        return render(request, template_name, context)
    else:
        form = PlanillaForm()
        return render(request, template_name, {'form': form})
