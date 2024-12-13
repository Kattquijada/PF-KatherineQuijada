from django import forms
from .models import ingresos,egresos,deuda

class ingresosform(forms.ModelForm):
    class Meta:
        model = ingresos
        fields = "__all__"

class egresosform(forms.ModelForm):
    class Meta:
        model = egresos
        fields = "__all__"

class deudaform(forms.ModelForm):
    class Meta:
        model = deuda
        fields = "__all__"