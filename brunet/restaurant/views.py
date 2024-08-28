from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Caja, Pedido, Reserva, Inventario, Proveedor, Compra, Mesa, Pago, TransaccionCaja
from .forms import (
    AperturaCajaForm, 
    CierreCajaForm, 
    PedidoForm, 
    ModificarPedidoForm, 
    PagoForm, 
    ModificarPagoForm, 
    ReservaForm, 
    ModificarReservaForm, 
    CompraForm, 
    ModificarCompraForm, 
    MesaForm, 
    ProveedorForm, 
    InventarioForm
)
from django.contrib.auth.models import User

# Home View
@login_required
def home(request):
    mesas = Mesa.objects.all()
    return render(request, 'home.html', {'mesas': mesas})

# Apertura de Caja
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
    return render(request, 'caja/apertura_caja.html', {'form': form})

# Cierre de Caja
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
    return render(request, 'caja/cierre_caja.html', {'form': form, 'caja': caja_abierta})

# Creación de Pedido
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
    return render(request, 'pedido/crear_pedido.html', {'form': form, 'mesa': mesa})

# Modificación de Pedido
@login_required
def modificar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        form = ModificarPedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido modificado con éxito.')
            return redirect('home')
    else:
        form = ModificarPedidoForm(instance=pedido)
    return render(request, 'pedido/modificar_pedido.html', {'form': form})

# Eliminación de Pedido
@login_required
def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado con éxito.')
        return redirect('home')
    return render(request, 'pedido/eliminar_pedido.html', {'pedido': pedido})

# Creación de Pago
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
    return render(request, 'pago/crear_pago.html', {'form': form, 'pedido': pedido})

# Modificación de Pago
@login_required
def modificar_pago(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    if request.method == 'POST':
        form = ModificarPagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pago modificado con éxito.')
            return redirect('home')
    else:
        form = ModificarPagoForm(instance=pago)
    return render(request, 'pago/modificar_pago.html', {'form': form})

# Eliminación de Pago
@login_required
def eliminar_pago(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    if request.method == 'POST':
        pago.delete()
        messages.success(request, 'Pago eliminado con éxito.')
        return redirect('home')
    return render(request, 'pago/eliminar_pago.html', {'pago': pago})

# Vista de Reservas
@login_required
def reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reserva/reservas.html', {'reservas': reservas})

# Creación de Reserva
@login_required
def crear_reserva(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.mesa = mesa
            reserva.save()
            messages.success(request, 'Reserva creada con éxito.')
            return redirect('home')
    else:
        form = ReservaForm()
    return render(request, 'reserva/crear_reserva.html', {'form': form, 'mesa': mesa})

# Modificación de Reserva
@login_required
def modificar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        form = ModificarReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva modificada con éxito.')
            return redirect('home')
    else:
        form = ModificarReservaForm(instance=reserva)
    return render(request, 'reserva/modificar_reserva.html', {'form': form})

# Eliminación de Reserva
@login_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva eliminada con éxito.')
        return redirect('home')
    return render(request, 'reserva/eliminar_reserva.html', {'reserva': reserva})

# Inventario
@login_required
def inventario(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventario/inventario.html', {'inventarios': inventarios})

# Creación de Inventario
def crear_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = InventarioForm()
    return render(request, 'inventario/crear_inventario.html', {'form': form})

# Edición de Inventario
def editar_inventario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'inventario/editar_inventario.html', {'form': form})

# Eliminación de Inventario
def eliminar_inventario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        inventario.delete()
        return redirect('inventario')
    return render(request, 'inventario/eliminar_inventario.html', {'inventario': inventario})

# Proveedores
@login_required
def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/proveedores.html', {'proveedores': proveedores})

# Creación de Proveedor
@login_required
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor agregado con éxito.')
            return redirect('proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedor/crear_proveedor.html', {'form': form})

# Edición de Proveedor
def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado con éxito.')
            return redirect('proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedor/editar_proveedor.html', {'form': form})

# Eliminación de Proveedor
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, 'Proveedor eliminado con éxito.')
        return redirect('proveedores')
    return render(request, 'proveedor/eliminar_proveedor.html', {'proveedor': proveedor})

# Compras
@login_required
def compras(request):
    compras = Compra.objects.all()
    return render(request, 'compra/compras.html', {'compras': compras})

# Creación de Compra
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
    return render(request, 'compra/crear_compra.html', {'form': form})

# Edición de Compra
@login_required
def editar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    if request.method == 'POST':
        form = ModificarCompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compra modificada con éxito.')
            return redirect('compras')
    else:
        form = ModificarCompraForm(instance=compra)
    return render(request, 'compra/editar_compra.html', {'form': form})

# Eliminación de Compra
@login_required
def eliminar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    if request.method == 'POST':
        compra.delete()
        messages.success(request, 'Compra eliminada con éxito.')
        return redirect('compras')
    return render(request, 'compra/eliminar_compra.html', {'compra': compra})

# Mesas
@login_required
def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesa/mesas.html', {'mesas': mesas})

def crear_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mesas')
    else:
        form = MesaForm()
    return render(request, 'mesa/crear_mesa.html', {'form': form})

def editar_mesa(request, pk):  
    mesa = get_object_or_404(Mesa, id=pk)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('lista_mesas')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'mesa/editar_mesa.html', {'form': form})

def eliminar_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    mesa.delete()
    return redirect('lista_mesas')

# Flujo de Caja

@login_required
def abrir_caja(request):
    if request.method == 'POST':
        total_inicial = request.POST.get('total_inicial')
        caja = Caja(usuario=request.user, total_inicial=total_inicial)
        caja.save()
        return redirect('consulta_caja', caja_id=caja.id)
    return render(request, 'caja/abrir_caja.html')

@login_required
def cerrar_caja(request, caja_id):
    caja = get_object_or_404(Caja, id=caja_id)
    if caja.estado == 'cerrada':
        return redirect('consulta_caja', caja_id=caja.id)
    
    if request.method == 'POST':
        total_final = request.POST.get('total_final')
        caja.cerrar_caja(total_final)
        return redirect('consulta_caja', caja_id=caja.id)
    return render(request, 'caja/cerrar_caja.html', {'caja': caja})

@login_required
def registrar_pago(request, pedido_id):
    caja_abierta = Caja.objects.filter(estado='abierta').first()
    if not caja_abierta:
        return redirect('abrir_caja')
    
    pedido = get_object_or_404(Pedido, id=pedido_id, estado='pendiente')
    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_pago')
        pago = Pago(pedido=pedido, metodo_pago=metodo_pago)
        pago.save()
        pedido.estado = 'pagado'
        pedido.save()

        # Registrar ingreso en la caja
        transaccion = TransaccionCaja(
            caja=caja_abierta,
            tipo='ingreso',
            monto=pago.monto,
            descripcion=f'Pago de pedido {pedido.id}'
        )
        transaccion.save()

        return redirect('consulta_caja', caja_id=caja_abierta.id)
    
    return render(request, 'caja/registrar_pago.html', {'pedido': pedido, 'caja': caja_abierta})

@login_required
def consulta_caja(request, caja_id):
    caja = get_object_or_404(Caja, id=caja_id)
    transacciones = TransaccionCaja.objects.filter(caja=caja)
    return render(request, 'caja/consulta_caja.html', {'caja': caja, 'transacciones': transacciones})

# Logger

from django.contrib.auth import views as auth_views
class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'  


#pagina para clinetes.
from django.shortcuts import render
from .models import Mesa, Menu  

def cliente(request):
    mesas = Mesa.objects.all() 
    menu_items = Menu.objects.all()  

    return render(request, 'restaurant/cliente.html', {
        'mesas': mesas,
        'menu_items': menu_items,
    })


#Menu "Platos."
from django.shortcuts import render, redirect
from .forms import MenuForm
from .models import Menu

@login_required
def crear_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)  # Asegúrate de manejar los archivos
        if form.is_valid():
            form.save()
            messages.success(request, 'El menú ha sido guardado con éxito.')
            return redirect('cliente')  # Redirigir a la página del cliente o donde prefieras
    else:
        form = MenuForm()
    return render(request, 'menu/menu.html', {'form': form})
