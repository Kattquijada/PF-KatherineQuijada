from django.contrib import messages
from django.contrib.auth.decorators import login_not_required, login_required
from django.urls import reverse_lazy
from django.utils import timezone 
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..models import deuda
from ..forms import deudaform, filtrodeudaForm


class deudaListView(ListView):
    model = deuda
    template_name = "control/vista_deuda.html"
    def get_queryset(self):
        queryset = deuda.objects.filter(usuario=self.request.user)
        form = filtrodeudaForm(self.request.GET)
        if form.is_valid():
            mes = form.cleaned_data['mes']
            anio = form.cleaned_data.get('anio')
            if not anio:
                anio = timezone.now().year
            queryset = queryset.filter(fecha_deuda__year=anio, fecha_deuda__month=mes).order_by('fecha_deuda')
        return queryset.order_by('fecha_deuda')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = filtrodeudaForm()
        return context


class deudaCreateView(CreateView):
    model = deuda
    form_class = deudaform
    success_url = reverse_lazy('control:form_deuda')
    template_name = "control/form_deuda.html"

    def form_valid(self, form):
        messages.success(self.request, 'Registro creado')
        return super().form_valid(form)


class deudaUpdateView(UpdateView):
    model = deuda
    form_class = deudaform
    success_url = reverse_lazy('control:vista_deuda')
    template_name = "control/form_deuda.html"

    def form_valid(self, form):
        messages.success(self.request, 'Registro actualizado exitosamente')
        return super().form_valid(form)

class deudaDetailView(DetailView):
    model = deuda
    template_name = "control/detail_deuda.html"


class deudaDeleteView(DeleteView):
    model = deuda
    success_url = reverse_lazy('control:vista_deuda')
    template_name = "control/delete_deuda.html"

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Registro eliminado exitosamente')
        return super().delete(request, *args, **kwargs)