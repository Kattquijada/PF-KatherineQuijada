from django import forms
from .models import ingresos,egresos,deuda

class ingresosform(forms.ModelForm):
    class Meta:
        model = ingresos
        fields = "__all__"
        widgets = {
            "fecha_ingreso": forms.DateInput(attrs={"type":"date"}),
        }

class egresosform(forms.ModelForm):
    class Meta:
        model = egresos
        fields = "__all__"
        widgets = {
            "fecha_deuda": forms.DateInput(attrs={"type":"date"}),
        }


class deudaform(forms.ModelForm):
    class Meta:
        model = deuda
        fields = "__all__"
        widgets = {
            "fecha_deuda": forms.DateInput(attrs={"type":"date"}),
        }
