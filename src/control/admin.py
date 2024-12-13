from django.contrib import admin

# Register your models here.
from .models import deuda,egresos,ingresos

@admin.register(ingresos)
class ingresosAdmin(admin.ModelAdmin):
    list_display = ("origen","tipo","fecha_ingreso","valor_ingreso",)

@admin.register(egresos)
class egresosAdmin(admin.ModelAdmin):
    list_display = ("gasto","fuente","fecha_gasto","valor_gasto",)

@admin.register(deuda)
class deudaAdmin(admin.ModelAdmin):
    list_display = ("deudas","entidad","fecha_deuda","valor_deuda","cuotas",)