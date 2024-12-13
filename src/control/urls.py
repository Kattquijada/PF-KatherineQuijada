from django.urls import path

from .views import index, about, vista_ingresos, form_ingresos, vista_egresos, form_egresos, vista_deuda, form_deuda

app_name = "control"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("ingresos/list/", vista_ingresos, name="vista_ingresos"),
    path("ingresos/form/", form_ingresos, name="form_ingresos"),
    path("egresos/list/", vista_egresos, name="vista_egresos"),
    path("egresos/form/", form_egresos, name="form_egresos"),
    path("deuda/list/", vista_deuda, name="vista_deuda"),
    path("deuda/form/", form_deuda, name="form_deuda"),    
]