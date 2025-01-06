from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone 
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..models import ingresos
from ..forms import ingresosform, filtroingresosForm

class ingresosListView(ListView):
    model = ingresos
    template_name = "control/vista_ingresos.html"
    def get_queryset(self):
        queryset = ingresos.objects.filter(usuario=self.request.user)
        form = filtroingresosForm(self.request.GET)
        if form.is_valid():
            mes = form.cleaned_data['mes']
            anio = form.cleaned_data.get('anio')
            if not anio:
                anio = timezone.now().year
            queryset = queryset.filter(fecha_ingreso__year=anio, fecha_ingreso__month=mes).order_by('fecha_ingreso')
        return queryset.order_by('fecha_ingreso')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = filtroingresosForm()
        return context

class ingresosCreateView(CreateView):
    model = ingresos
    form_class = ingresosform
    success_url = reverse_lazy('control:form_ingresos')
    template_name = "control/form_ingresos.html"

    def form_valid(self, form):
        messages.success(self.request, 'Registro creado')
        return super().form_valid(form)


class ingresosUpdateView(UpdateView):
    model = ingresos
    form_class = ingresosform
    success_url = reverse_lazy('control:vista_ingresos')
    template_name = "control/form_ingresos.html"

    def form_valid(self, form):
        messages.success(self.request, 'Registro actualizado exitosamente')
        return super().form_valid(form)


class ingresosDetailView(DetailView):
    model = ingresos
    template_name = "control/detail_ingresos.html"


class ingresosDeleteView(DeleteView):
    model = ingresos
    success_url = reverse_lazy('control:vista_ingresos')
    template_name = "control/delete_ingresos.html"

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Registro eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
