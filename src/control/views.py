from django.shortcuts import render, redirect
from .models import ingresos,egresos,deuda
from .forms import ingresosform, egresosform, deudaform
# Create your views here.

def index(request):
    return render(request,"control/index.html")

def about(request):
    return render(request,"control/about.html")

def vista_ingresos(request):
    query = ingresos.objects.all()
    context = {"object_list":query}
    return render(request,"control/vista_ingresos.html", context)

def form_ingresos(request):
    if request.method == "GET":
        form = ingresosform()
    if request.method == "POST":
        form = ingresosform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("control:form_ingresos")
    return render(request,"control/form_ingresos.html", {"form":form})

def vista_egresos(request):
    query = egresos.objects.all()
    context = {"object_list":query}
    return render(request,"control/vista_egresos.html", context)

def form_egresos(request):
    if request.method == "GET":
        form = egresosform()
    if request.method == "POST":
        form = egresosform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("control:form_egresos")
    return render(request,"control/form_egresos.html", {"form":form})

def vista_deuda(request):
    query = deuda.objects.all()
    context = {"object_list":query}
    return render(request,"control/vista_deuda.html", context)

def form_deuda(request):
    if request.method == "GET":
        form = deudaform()
    if request.method == "POST":
        form = deudaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("control:form_deuda")
    return render(request,"control/form_deuda.html", {"form":form})