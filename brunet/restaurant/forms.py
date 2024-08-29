from django import forms
from .models import Caja, Pedido, Pago, Reserva, Compra, Mesa, Proveedor, Inventario

# Formulario para Apertura de Caja
class AperturaCajaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = ['total_inicial']

# Formulario para Cierre de Caja
class CierreCajaForm(forms.ModelForm):
    total_final = forms.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Caja
        fields = ['total_final']

# Formulario para Pedido
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['usuario', 'mesa', 'total', 'estado']  # Incluye campos adicionales necesarios

# Formulario para Modificar Pedido
class ModificarPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['usuario', 'mesa', 'estado', 'total']  

# Formulario para Pago
class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['metodo_pago']

# Formulario para Modificar Pago
class ModificarPagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['metodo_pago', 'monto']  # Incluye el campo para modificar el monto si es necesario

# Formulario para Reserva
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['mesa', 'fecha_reserva', 'nombre_cliente', 'telefono_cliente', 'estado']

# Formulario para Modificar Reserva
class ModificarReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['mesa', 'fecha_reserva', 'nombre_cliente', 'telefono_cliente', 'estado']

# Formulario para Compra
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor', 'total', 'tiene_documentacion', 'archivo_documentacion', 'detalle']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'tiene_documentacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'archivo_documentacion': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

# Formulario para Modificar Compra
class ModificarCompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor', 'total']

# Formulario para Mesa
class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero_mesa', 'capacidad', 'estado']

# Formulario para Proveedor
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_proveedor', 'contact_method', 'telefono', 'email']
        labels = {
            'nombre_proveedor': 'Nombre del Proveedor',
            'contact_method': 'Método de Contacto',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'nombre_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_method': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# Formulario para Inventario
class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre_producto', 'cantidad_actual', 'cantidad_minima', 'unidad_medida']

# Fromulario de menu
from django import forms
from .models import Menu
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['nombre_plato', 'descripcion', 'precio', 'disponible', 'imagen']  
        
        
#flujo de pedido por si tiene algun problema ver aca chicos.!
        