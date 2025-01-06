from django.contrib import messages
from django import forms
from django.urls import reverse_lazy
from django.utils import timezone 
from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..models import egresos
from ..forms import egresosform, filtroegresosForm

class egresosListView(ListView):
    model = egresos
    template_name = "control/vista_egresos.html"
    def get_queryset(self):
        queryset = egresos.objects.filter(usuario=self.request.user)
        form = filtroegresosForm(self.request.GET)
        if form.is_valid():
            mes = form.cleaned_data['mes']
            anio = form.cleaned_data.get('anio')
            if not anio:
                anio = timezone.now().year
            queryset = queryset.filter(fecha_gasto__year=anio, fecha_gasto__month=mes).order_by('fecha_gasto')
        return queryset.order_by('fecha_gasto')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = filtroegresosForm()
        return context
    
class egresosCreateView(CreateView):
    model = egresos
    form_class = egresosform
    success_url = reverse_lazy('control:form_egresos')
    template_name = "control/form_egresos.html"
       
    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Set user before saving
        form.fields['usuario'].widget = forms.HiddenInput()  # Hide the field
        messages.success(self.request, 'Registro creado')
        return super().form_valid(form)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class egresosUpdateView(UpdateView):
    model = egresos
    form_class = egresosform
    success_url = reverse_lazy('control:vista_egresos')
    template_name = "control/form_egresos.html"

    def form_valid(self, form):
        messages.success(self.request, 'Registro actualizado exitosamente')
        return super().form_valid(form)


class egresosDetailView(DetailView):
    model = egresos
    template_name = "control/detail_egresos.html"


class egresosDeleteView(DeleteView):
    model = egresos
    success_url = reverse_lazy('control:vista_egresos')
    template_name = "control/delete_egresos.html"

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Registro eliminado exitosamente')
        return super().delete(request, *args, **kwargs)