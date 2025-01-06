from django.urls import path
from django.contrib.auth.views import LogoutView

from  .views import *
from control.views_models import ingresos, egresos, deuda, resumen

app_name = "control"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("perfil", perfil, name="perfil"),
    path("login/", customLoginView.as_view(), name="login"),
    path("logout/",LogoutView.as_view(template_name="control/logout.html"), name="logout"),
    path("registro/",CustomRegisterView.as_view(template_name="control/registro.html"), name="registro"),
    path("editarperfil/",UpdateProfileView.as_view(template_name="control/editar_perfil.html"), name="editar perfil"),
    path("resumen/",resumen.resumen_financiero, name="resumen_financiero"),

]
urlpatterns += [   
    path("ingresos/list/", ingresos.ingresosListView.as_view(), name="vista_ingresos"),
    path("ingresos/form/", ingresos.ingresosCreateView.as_view(), name="form_ingresos"),
    path("ingresos/update/<int:pk>", ingresos.ingresosUpdateView.as_view(), name="update_ingresos"),
    path("ingresos/detail/<int:pk>", ingresos.ingresosDetailView.as_view(), name="detail_ingresos"),
    path("ingresos/delete/<int:pk>", ingresos.ingresosDeleteView.as_view(), name="delete_ingresos"),
]
urlpatterns += [    
    path("egresos/list/", egresos.egresosListView.as_view(), name="vista_egresos"),
    path("egresos/form/", egresos.egresosCreateView.as_view(), name="form_egresos"),
    path("eresos/update/<int:pk>", egresos.egresosUpdateView.as_view(), name="update_egresos"),
    path("egresos/detail/<int:pk>", egresos.egresosDetailView.as_view(), name="detail_egresos"),
    path("egresos/delete/<int:pk>", egresos.egresosDeleteView.as_view(), name="delete_egresos"),
]
urlpatterns += [    
    path("deuda/list/", deuda.deudaListView.as_view(), name="vista_deuda"),
    path("deuda/form/", deuda.deudaCreateView.as_view(), name="form_deuda"),
    path("deuda/update/<int:pk>", deuda.deudaUpdateView.as_view(), name="update_deuda"),
    path("deuda/detail/<int:pk>", deuda.deudaDetailView.as_view(), name="detail_deuda"),
    path("deuda/delete/<int:pk>", deuda.deudaDeleteView.as_view(), name="delete_deuda"),
]