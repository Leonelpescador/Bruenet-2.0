from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Caja, Pedido, Reserva, Inventario, Proveedor, Compra, Mesa
from .forms import AperturaCajaForm, CierreCajaForm, PedidoForm, PagoForm, ReservaForm, CompraForm

@login_required
def home(request):
    mesas = Mesa.objects.all()
    return render(request, 'restaurant/home.html', {'mesas': mesas})

@login_required
def apertura_caja(request):
    if request.method == 'POST':
        form = AperturaCajaForm(request.POST)
        if form.is_valid():
            caja = form.save(commit=False)
            caja.usuario = request.user
            caja.save()
            messages.success(request, 'Caja abierta con éxito.')
            return redirect('home')
    else:
        form = AperturaCajaForm()
    return render(request, 'restaurant/apertura_caja.html', {'form': form})

@login_required
def cierre_caja(request):
    caja_abierta = Caja.objects.filter(cierre__isnull=True).first()
    if request.method == 'POST':
        form = CierreCajaForm(request.POST, instance=caja_abierta)
        if form.is_valid():
            total_final = form.cleaned_data['total_final']
            caja_abierta.cerrar_caja(total_final)
            messages.success(request, 'Caja cerrada con éxito.')
            return redirect('home')
    else:
        form = CierreCajaForm(instance=caja_abierta)
    return render(request, 'restaurant/cierre_caja.html', {'form': form, 'caja': caja_abierta})

@login_required
def crear_pedido(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.mesa = mesa
            pedido.save()
            messages.success(request, 'Pedido creado con éxito.')
            return redirect('home')
    else:
        form = PedidoForm()
    return render(request, 'restaurant/crear_pedido.html', {'form': form, 'mesa': mesa})

@login_required
def crear_pago(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.pedido = pedido
            pago.save()
            messages.success(request, 'Pago realizado con éxito.')
            return redirect('home')
    else:
        form = PagoForm()
    return render(request, 'restaurant/crear_pago.html', {'form': form, 'pedido': pedido})

@login_required
def reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'restaurant/reservas.html', {'reservas': reservas})

@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            messages.success(request, 'Reserva creada con éxito.')
            return redirect('reservas')
    else:
        form = ReservaForm()
    return render(request, 'restaurant/crear_reserva.html', {'form': form})

@login_required
def inventario(request):
    inventarios = Inventario.objects.all()
    return render(request, 'restaurant/inventario.html', {'inventarios': inventarios})

@login_required
def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'restaurant/proveedores.html', {'proveedores': proveedores})

@login_required
def compras(request):
    compras = Compra.objects.all()
    return render(request, 'restaurant/compras.html', {'compras': compras})

@login_required
def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            messages.success(request, 'Compra registrada con éxito.')
            return redirect('compras')
    else:
        form = CompraForm()
    return render(request, 'restaurant/crear_compra.html', {'form': form})


#Logger

from django.contrib.auth import views as auth_views
class CustomLoginView(auth_views.LoginView):
    template_name = 'restaurant/login.html'  # Tu propia plantilla de inicio de sesión
#----------------------Logger-------------------------------------------------#