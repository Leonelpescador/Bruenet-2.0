from django import forms
from .models import Caja, Pedido, Pago, Reserva, Compra

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
