from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class ingresos(models.Model):
    origen_choice = [
        ("Sueldo","Sueldo"),
        ("Otro","Otro"),
    ]
    tipo_choice = [
        ("Cta Corriente","Cuenta Corriente"),
        ("Efectivo","Efectivo"),
    ]
    origen = models.CharField(max_length=6, choices=origen_choice)
    tipo = models.CharField(max_length=15, choices=tipo_choice)
    fecha_ingreso = models.DateField()
    valor_ingreso = models.PositiveIntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class egresos(models.Model):
    gasto_choice = [
        ("Servicios Básicos","Servicios Básicos"),
        ("Necesidades","Necesidades"),
        ("Mascotas","Mascotas"),
        ("Compra en crédito","Compra en crédito"),
        ("Prestamos","Prestamos"),
        ("Caprichos","Caprichos"),
        ("Otros","Otros"),
    ]
    fuente_choice = [
        ("Cuenta Corriente","Cuenta Corriente"),
        ("Efectivo","Efectivo"),
    ]
    gasto = models.CharField(max_length=20, choices=gasto_choice)
    fuente = models.CharField(max_length=20, choices=fuente_choice)
    fecha_gasto = models.DateField()
    valor_gasto = models.PositiveIntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

class deuda(models.Model):
    deudas_choice = [
        ("Crédito Consumo","Crédito Consumo"),
        ("Crédito Hipotecario","Crédito Hipotecario"),
        ("Compra en crédito","Compra en crédito"),
        ("Prestamos","Prestamos"),
        ("Otros","Otros"),
    ]
    entidad_choice = [
        ("Itau","Itau"),
        ("Scotiabank","Scotiabank"),
        ("Particulares","Particulares"),
        ("Otro","Otro")
    ]
    deudas = models.CharField(max_length=20, choices=deudas_choice)
    entidad = models.CharField(max_length=20, choices=entidad_choice)
    fecha_deuda = models.DateField()
    valor_deuda = models.PositiveIntegerField()
    cuotas = models.PositiveIntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)