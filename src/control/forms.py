from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import ingresos,egresos,deuda


class ingresosform(forms.ModelForm):
    class Meta:
        model = ingresos
        fields = "__all__"
        widgets = {
            "fecha_ingreso": forms.DateInput(attrs={"type":"date"}),
            "otros_ingreso": forms.Textarea(attrs={"placeholder":"Ingrese detalle otra fuente de ingresos"})
        }

class egresosform(forms.ModelForm):
    class Meta:
        model = egresos
        fields = "__all__"
        widgets = {
            "fecha_gasto": forms.DateInput(attrs={"type":"date"}),
        }


class deudaform(forms.ModelForm):
    class Meta:
        model = deuda
        fields = "__all__"
        widgets = {
            "fecha_deuda": forms.DateInput(attrs={"type":"date"}),
        }
        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(VentaForm, self).__init__(*args, **kwargs)
            if self.user:
                usuario = usuario.objects.get(usuario=self.user)
                self.fields['usuario'] = forms.CharField(
                    initial=usuario.usuario.username,
                    widget=forms.TextInput(attrs={'readonly': 'readonly'}),
                )

class filtroingresosForm(forms.Form):
    mes = forms.IntegerField(min_value=1, max_value=12, label='Mes')
    anio = forms.IntegerField(label='Año', required=False)

class filtroegresosForm(forms.Form):
    mes = forms.IntegerField(min_value=1, max_value=12, label='Mes')
    anio = forms.IntegerField(label='Año', required=False)

class filtrodeudaForm(forms.Form):
    mes = forms.IntegerField(min_value=1, max_value=12, label='Mes')
    anio = forms.IntegerField(label='Año', required=False)

class customAuthenticationForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {'username': ''}

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']