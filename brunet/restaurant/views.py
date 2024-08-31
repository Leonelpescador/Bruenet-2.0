from .forms import ModificarPedidoForm  
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
    caja = Caja.objects.filter(estado='abierta').first()

    context = {
        'mesas': mesas,
        'caja_abierta': caja,
    }

    return render(request, 'home.html', context)


# Creación de Pedido aca comienza
from .models import DetallePedido
from .forms import PedidoForm, DetallePedidoForm
from django.forms import inlineformset_factory

from django.forms import inlineformset_factory
from .models import Pedido, DetallePedido

# Formset para DetallePedido
DetallePedidoFormSet = inlineformset_factory(Pedido, DetallePedido, form=DetallePedidoForm, extra=1)


from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pedido, DetallePedido, Mesa
from .forms import PedidoForm, DetallePedidoForm, ModificarPedidoForm
from django.contrib.auth.decorators import login_required



@login_required
@login_required
def crear_pedido(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    PedidoFormSet = inlineformset_factory(Pedido, DetallePedido, form=DetallePedidoForm, extra=1)

    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        formset = PedidoFormSet(request.POST)

        if pedido_form.is_valid() and formset.is_valid():
            pedido = pedido_form.save(commit=False)
            pedido.usuario = request.user
            pedido.mesa = mesa
            pedido.save()

            # Guardar cada detalle del pedido
            for form in formset:
                detalle_pedido = form.save(commit=False)
                detalle_pedido.pedido = pedido
                detalle_pedido.save()

            # Calcular el total del pedido
            pedido.total = sum(detalle.subtotal for detalle in pedido.detalles.all())
            pedido.save()

            messages.success(request, 'Pedido creado con éxito.')
            return redirect('pedidos_activos')
    else:
        pedido_form = PedidoForm()
        formset = PedidoFormSet()

    categorias = Categoria.objects.all()

    return render(request, 'pedido/crear_pedido.html', {
        'pedido_form': pedido_form,
        'formset': formset,
        'mesa': mesa,
        'categorias': categorias,
    })

@login_required
def modificar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    PedidoFormSet = inlineformset_factory(Pedido, DetallePedido, form=DetallePedidoForm, extra=0)

    if request.method == 'POST':
        pedido_form = ModificarPedidoForm(request.POST, instance=pedido)
        formset = PedidoFormSet(request.POST, instance=pedido)

        if pedido_form.is_valid() and formset.is_valid():
            pedido_form.save()
            formset.save()

            # Recalcular el total del pedido
            pedido.total = sum(detalle.subtotal for detalle in pedido.detalles.all())
            pedido.save()

            messages.success(request, 'Pedido modificado con éxito.')
            return redirect('pedidos_activos')
    else:
        pedido_form = ModificarPedidoForm(instance=pedido)
        formset = PedidoFormSet(instance=pedido)

    categorias = Categoria.objects.all()

    return render(request, 'pedido/modificar_pedido.html', {
        'pedido_form': pedido_form,
        'formset': formset,
        'pedido': pedido,
        'categorias': categorias,
    })


@login_required
def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado con éxito.')
        return redirect('home')
    
    return render(request, 'pedido/eliminar_pedido.html', {'pedido': pedido})

@login_required
def pedidos_activos(request):
    pedidos = Pedido.objects.filter(estado__in=['pendiente', 'preparando', 'servido'])
    return render(request, 'pedido/pedidos_activos.html', {'pedidos': pedidos})


from django.http import JsonResponse
from .models import Menu

def obtener_precio_plato(request):
    menu_id = request.GET.get('menu_id')
    if menu_id:
        try:
            plato = Menu.objects.get(id=menu_id)
            return JsonResponse({'precio': plato.precio})
        except Menu.DoesNotExist:
            return JsonResponse({'error': 'Plato no encontrado'}, status=404)
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)


#fin pedidos

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


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm, ModificarReservaForm
from .models import Reserva

# Creación de Reserva
@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)  # No guardar aún en la base de datos
            reserva.usuario = request.user  # Asignar el usuario actual
            reserva.save()  # Ahora guardar en la base de datos
            messages.success(request, 'Reserva creada con éxito.')
            return redirect('reservas')  # Redirige a la lista de reservas o donde sea necesario
    else:
        form = ReservaForm()
    return render(request, 'reserva/crear_reserva.html', {'form': form})

#modifcar reserva
@login_required
def modificar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        form = ModificarReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva modificada con éxito.')
            return redirect('reservas')
    else:
        form = ModificarReservaForm(instance=reserva)
    return render(request, 'reserva/editar_reserva.html', {'form': form})


# Eliminación de Reserva
@login_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva eliminada con éxito.')
        return redirect('reservas')  # Redirige a la lista de reservas o donde sea necesario
    return render(request, 'reserva/eliminar_reserva.html', {'reserva': reserva})


#from de reservas  
from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    fecha_reserva = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Fecha y Hora de la Reserva'
    )

    class Meta:
        model = Reserva
        fields = ['mesa', 'fecha_reserva', 'nombre_cliente', 'telefono_cliente', 'estado', 'numero_personas', 'comentarios']

class ModificarReservaForm(forms.ModelForm):
    fecha_reserva = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Fecha y Hora de la Reserva'
    )

    class Meta:
        model = Reserva
        fields = ['mesa', 'fecha_reserva', 'nombre_cliente', 'telefono_cliente', 'estado', 'numero_personas', 'comentarios']


#fin de flujo de reserva.






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
    return render(request, 'proveedores/proveedores.html', {'proveedores': proveedores})

# Creación de Proveedor
@login_required
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    else:
        form = ProveedorForm()
    
    return render(request, 'proveedores/crear_proveedores.html', {'form': form})

# Edición de Proveedor
@login_required
def editar_proveedor(request, pk):
    proveedor = Proveedor.objects.get(pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    else:
        form = ProveedorForm(instance=proveedor)

    return render(request, 'proveedores/editar_proveedores.html', {'form': form})


# Eliminación de Proveedor
@login_required
def eliminar_proveedor(request, pk):
    proveedor = Proveedor.objects.get(pk=pk)
    if request.method == "POST":
        proveedor.delete()
        return redirect('proveedores')
    
    return render(request, 'proveedores/eliminar_proveedores.html', {'proveedor': proveedor})

# Compras
from django.shortcuts import render, redirect
from .models import Compra
from .forms import CompraForm

def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('compras')
    else:
        form = CompraForm()
    
    return render(request, 'compra/crear_compra.html', {'form': form})

def compras(request):
    compras = Compra.objects.all()
    for compra in compras:
        # Determinamos si el archivo adjunto es un PDF
        if compra.archivo_documentacion:
            compra.es_pdf = compra.archivo_documentacion.url.lower().endswith('.pdf')
        else:
            compra.es_pdf = False
    
    return render(request, 'compra/compras.html', {'compras': compras})

@login_required
def editar_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        form = CompraForm(request.POST, request.FILES, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('compras')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'compra/editar_compra.html', {'form': form})
@login_required
def eliminar_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        compra.delete()
        return redirect('compras')
    return render(request, 'compra/eliminar_compra.html', {'compra': compra})
# Mesas
@login_required
def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesa/mesas.html', {'mesas': mesas})
@login_required
def crear_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mesas')
    else:
        form = MesaForm()
    return render(request, 'mesa/crear_mesa.html', {'form': form})
@login_required
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
@login_required
def eliminar_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    mesa.delete()
    return redirect('lista_mesas')


# Flujo de Caja
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from .models import Caja, Pago, Pedido, TransaccionCaja
from django.contrib.auth.decorators import login_required

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
            return redirect('consulta_caja', caja_id=caja.id)
    else:
        form = AperturaCajaForm()
    return render(request, 'caja/apertura_caja.html', {'form': form})

# Consulta de Caja
@login_required
def consulta_caja(request, caja_id):
    caja = get_object_or_404(Caja, id=caja_id)
    transacciones = TransaccionCaja.objects.filter(caja=caja)

    # Filtrar pagos asociados a los pedidos que se realizaron durante la apertura de la caja si lo sacan le va dar error 
    pedidos_en_caja = Pedido.objects.filter(fecha_pedido__gte=caja.apertura, fecha_pedido__lte=caja.cierre if caja.cierre else timezone.now())
    pagos = Pago.objects.filter(pedido__in=pedidos_en_caja)
    
    monto_total = pagos.aggregate(total=Sum('monto'))['total'] or 0
    
    return render(request, 'caja/consulta_caja.html', {
        'caja': caja,
        'transacciones': transacciones,
        'monto_total': monto_total,
        'pagos': pagos
    })


# Cierre de Caja
@login_required
def cierre_caja(request, caja_id):
    caja = get_object_or_404(Caja, id=caja_id)

    if request.method == 'POST':
        total_final = caja.calcular_total_final()
        caja.cerrar_caja(total_final)
        messages.success(request, f'Caja {caja.id} cerrada exitosamente con un total de {caja.total_final}.')
        return redirect('home')  # Redirige a la vista deseada después de cerrar la caja

    total_final = caja.calcular_total_final()
    total_ingresos = sum(transaccion.monto for transaccion in caja.transacciones.filter(tipo='ingreso'))
    
    return render(request, 'caja/cierre_caja.html', {
        'caja': caja,
        'total_final': total_final,
        'total_ingresos': total_ingresos,
    })




# Registrar Pago

@login_required
def registrar_pago(request, pedido_id):
    caja_abierta = Caja.objects.filter(estado='abierta').first()
    if not caja_abierta:
        return redirect('apertura_caja')

    pedido = get_object_or_404(Pedido, id=pedido_id, estado='pendiente')
    
    if not pedido:
        messages.error(request, 'No se encontró un pedido válido para registrar el pago.')
        return redirect('home')

    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_pago')
        pago = Pago(pedido=pedido, metodo_pago=metodo_pago, monto=pedido.total)
        pago.save()
        pedido.estado = 'pagado'
        pedido.save()

        transaccion = TransaccionCaja(
            caja=caja_abierta,
            tipo='ingreso',
            monto=pago.monto,
            descripcion=f'Pago de pedido {pedido.id}'
        )
        transaccion.save()

        return redirect('consulta_caja', caja_id=caja_abierta.id)
    
    return render(request, 'caja/registrar_pago.html', {'pedido': pedido, 'caja': caja_abierta})



#reporte de cierre de caja 
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import io
from django.utils import timezone

def descargar_reporte_caja(request, caja_id):
    caja = get_object_or_404(Caja, id=caja_id)
    template_path = 'caja/reporte_caja_pdf.html'
    context = {'caja': caja}
    
    # Verificar si la caja tiene una fecha de cierre
    if caja.cierre:
        fecha_cierre = caja.cierre.strftime("%Y-%m-%d_%H-%M-%S")
    else:
        # Si la caja no está cerrada, usar la fecha y hora actual
        fecha_cierre = timezone.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    nombre_archivo = f"Cierre_de_caja_{fecha_cierre}.pdf"
    
    # Renderizar la plantilla en un string
    html_string = render_to_string(template_path, context)
    
    # Crear un objeto de BytesIO para generar el PDF
    pdf = io.BytesIO()
    
    # Crear el PDF
    pisa_status = pisa.CreatePDF(
        io.StringIO(html_string),
        dest=pdf
    )
    
    # Si no hubo errores, preparar la respuesta con el PDF
    if not pisa_status.err:
        pdf.seek(0)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
        return response
    
    # Si hubo un error, mostrar el error en la respuesta
    return HttpResponse(f"Error al generar el PDF: {pisa_status.err}", content_type='text/plain')







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
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MenuForm
from .models import Menu
from django.contrib.auth.decorators import login_required

@login_required
def listar_menu(request):
    # Agrupar los menús por categoría
    categorias = Menu.objects.values_list('categoria__nombre', flat=True).distinct()
    menu_categorias = {categoria: Menu.objects.filter(categoria__nombre=categoria, disponible=True) for categoria in categorias}
    menu_items_no_disponibles = Menu.objects.filter(disponible=False)

    return render(request, 'menu/listar_menu.html', {
        'menu_categorias': menu_categorias,
        'menu_items_no_disponibles': menu_items_no_disponibles
    })

from .models import Categoria
@login_required
def crear_menu(request):
    categorias = Categoria.objects.all()  # Obtener todas las categorías
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'El menú ha sido guardado con éxito.')
            return redirect('listar_menu')
        else:
            messages.error(request, 'Error al guardar el menú. Verifica los datos ingresados.')
    else:
        form = MenuForm()

    return render(request, 'menu/crear_menu.html', {'form': form, 'categorias': categorias})

@login_required
def editar_menu(request, menu_id):
    menu_item = get_object_or_404(Menu, id=menu_id)
    categorias = Categoria.objects.all()  # Obtener todas las categorías
    
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu_item)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Plato actualizado con éxito.')
            return redirect('listar_menu')
    else:
        form = MenuForm(instance=menu_item)
    
    return render(request, 'menu/editar_menu.html', {
        'form': form, 
        'menu': menu_item,
        'categorias': categorias  # Pasar las categorías al contexto
    })

@login_required
def eliminar_menu(request, menu_id):
    menu_item = get_object_or_404(Menu, id=menu_id)
    if request.method == 'POST':
        menu_item.delete()
        messages.success(request, 'Plato eliminado con éxito.')
        return redirect('listar_menu')
    return render(request, 'menu/eliminar_menu.html', {'menu': menu_item})

@login_required
def cambiar_disponibilidad_menu(request, menu_id):
    menu_item = get_object_or_404(Menu, id=menu_id)
    menu_item.disponible = not menu_item.disponible
    menu_item.save()
    messages.success(request, 'La disponibilidad del menú ha sido actualizada.')
    return redirect('listar_menu')

from django.http import HttpResponse
from .models import Menu

def filtrar_platos_por_categoria(request):
    categoria_id = request.GET.get('categoria_id')
    if categoria_id:
        platos = Menu.objects.filter(categoria_id=categoria_id, disponible=True)
        opciones = ''.join([f'<option value="{plato.id}">{plato.nombre_plato}</option>' for plato in platos])
        return HttpResponse(opciones)
    return HttpResponse('<option value="">No hay platos disponibles</option>')


#fin menu.


#pagos.

@login_required
def crear_pago(request):
    caja_abierta = Caja.objects.filter(estado='abierta').first()
    if not caja_abierta:
        messages.error(request, 'Debe abrir una caja antes de registrar pagos.')
        return redirect('apertura_caja')

    pedidos_pendientes = Pedido.objects.filter(estado='pendiente')

    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.caja = caja_abierta
            pago.save()
            messages.success(request, 'Pago registrado exitosamente.')
            return redirect('consulta_caja', caja_id=caja_abierta.id)
    else:
        form = PagoForm()

    return render(request, 'caja/crear_pago.html', {'form': form, 'pedidos': pedidos_pendientes})

@login_required
def modificar_pago(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    if request.method == 'POST':
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pago modificado exitosamente.')
            return redirect('consulta_caja', caja_id=pago.caja.id)
    else:
        form = PagoForm(instance=pago)

    return render(request, 'caja/modificar_pago.html', {'form': form, 'pago': pago})

@login_required
def eliminar_pago(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    if request.method == 'POST':
        pago.delete()
        messages.success(request, 'Pago eliminado exitosamente.')
        return redirect('consulta_caja', caja_id=pago.caja.id)

    return render(request, 'caja/eliminar_pago.html', {'pago': pago})