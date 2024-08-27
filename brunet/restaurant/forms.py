from django import forms
from .models import Caja, Pedido, Pago, Reserva, Compra , Mesa,  Proveedor , Inventario

class AperturaCajaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = ['total_inicial']

class CierreCajaForm(forms.ModelForm):
    total_final = forms.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Caja
        fields = ['total_final']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['total']

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['metodo_pago']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['mesa', 'fecha_reserva', 'nombre_cliente', 'telefono_cliente', 'estado']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor', 'total']



class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero_mesa', 'capacidad', 'estado']
        


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_proveedor', 'contacto', 'telefono', 'email']


Inventario

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre_producto', 'cantidad_actual', 'cantidad_minima', 'unidad_medida']


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero_mesa', 'capacidad', 'estado']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'telefono_cliente', 'fecha_reserva']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['usuario', 'mesa', 'estado']
