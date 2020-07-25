from django.contrib import admin

from .models import plan, Planilla, Clientes

admin.site.register(plan)
admin.site.register(Planilla)
admin.site.register(Clientes)
