from django.shortcuts import render
from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.forms import BaseModelForm

from .forms import customAuthenticationForm,UserProfileForm,CustomUserCreationForm

# Create your views here.
@login_not_required
def index(request):
    return render(request,"control/index.html")

@login_not_required
def about(request):
    return render(request,"control/about.html")


class customLoginView(LoginView):
    authentication_form = customAuthenticationForm
    template_name = 'control/login.html'
    next_page = reverse_lazy('control:index')

    def form_valid(self, form: authentication_form) -> HttpResponse:
        usuario = form.get_user()
        messages.success(
            self.request, f'Sesión Iniciada{usuario.username}'
        )
        return super().form_valid(form)

@method_decorator(login_not_required, name='dispatch')  
class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'control/registro.html'
    success_url = reverse_lazy('control:login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Registro exitoso.')
        return super().form_valid(form)


class UpdateProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'control/editar_perfil.html'
    success_url = reverse_lazy('control:perfil')

    def get_object(self):
        # Devuelve el usuario actual en lugar de esperar un pk
        return self.request.user  

def perfil(request):
    return render(request,"control/perfil.html")

