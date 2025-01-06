from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.contrib.auth.models import User
import datetime
from ..models import ingresos, egresos

def resumen_financiero(request):
    # Get selected month from request, default to current month
    selected_month = request.GET.get('month', datetime.datetime.now().strftime('%Y-%m'))
    year, month = map(int, selected_month.split('-'))
    
    # Filter data for selected month
    user = request.user
    ingresos_mes = ingresos.objects.filter(
        fecha_ingreso__year=year,
        fecha_ingreso__month=month,
        usuario = user
      
    )
    egresos_mes = egresos.objects.filter(
        fecha_gasto__year=year,
        fecha_gasto__month=month,
        usuario = user
    )
    
    # Calculate totals
    total_ingresos = ingresos_mes.aggregate(total=Sum('valor_ingreso'))['total'] or 0
    total_egresos = egresos_mes.aggregate(total=Sum('valor_gasto'))['total'] or 0
    saldo = total_ingresos - total_egresos
    
    # Get expenses by type
    gastos_por_tipo = egresos_mes.values('gasto').annotate(
        total=Sum('valor_gasto')
    ).order_by('-total')
    
    # Get months for filter dropdown
    meses_disponibles = ingresos.objects.filter(usuario = user).dates('fecha_ingreso', 'month')
    
    # Prepare data for chart
    chart_data = list(gastos_por_tipo)
    
    context = {
        'selected_month': selected_month,
        'meses_disponibles': meses_disponibles,
        'total_ingresos': total_ingresos,
        'total_egresos': total_egresos,
        'saldo': saldo,
        'gastos_por_tipo': gastos_por_tipo,
        'chart_data': chart_data,
    }
    
    return render(request, 'control/resumen_financiero.html', context)