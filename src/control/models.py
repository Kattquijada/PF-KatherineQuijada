from django.db import models

# Create your models here.
class ingresos(models.Model):
    origen_choice = [
        ("Sueldo","Sueldo"),
        ("Otro","Otro"),
    ]
    origen = models.CharField(max_length=6, choices=origen_choice)
    tipo_choice = [
        ("Cta Corriente","Cuenta Corriente"),
        ("Efectivo","Efectivo"),
    ]
    tipo = models.CharField(max_length=15, choices=tipo_choice)
    fecha_ingreso = models.DateField()
    valor_ingreso = models.IntegerField()

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
    gasto = models.CharField(max_length=20, choices=gasto_choice)
    fuente_choice = [
        ("Itau","Itau"),
        ("Scotiabank","Scotiabank"),
    ]
    fuente = models.CharField(max_length=15, choices=fuente_choice)
    fecha_gasto = models.DateField()
    valor_gasto = models.IntegerField()

class deuda(models.Model):
    deudas_choice = [
        ("Crédito Consumo","Crédito Consumo"),
        ("Crédito Hipotecario","Crédito Hipotecario"),
        ("Compra en crédito","Compra en crédito"),
        ("Prestamos","Prestamos"),
        ("Otros","Otros"),
    ]
    deudas = models.CharField(max_length=20, choices=deudas_choice)
    entidad_choice = [
        ("Itau","Itau"),
        ("Scotiabank","Scotiabank"),
        ("Familia","Familia"),
    ]
    entidad = models.CharField(max_length=15, choices=entidad_choice)
    fecha_deuda = models.DateField()
    valor_deuda = models.IntegerField()
    cuotas = models.IntegerField()