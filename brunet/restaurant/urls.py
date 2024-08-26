from django.urls import path
from .views import CustomLoginView
from . import views
from .views import lista_mesas, crear_mesa, editar_mesa, eliminar_mesa, crear_proveedor, editar_proveedor, eliminar_proveedor

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('', views.home, name='home'),
    path('apertura-caja/', views.apertura_caja, name='apertura_caja'),
    path('cierre-caja/', views.cierre_caja, name='cierre_caja'),
    path('pedido/crear/<int:mesa_id>/', views.crear_pedido, name='crear_pedido'),
    path('pago/crear/<int:pedido_id>/', views.crear_pago, name='crear_pago'),
    path('reservas/', views.reservas, name='reservas'),
    path('reserva/crear/', views.crear_reserva, name='crear_reserva'),
    path('inventario/', views.inventario, name='inventario'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('compras/', views.compras, name='compras'),
    path('compra/crear/', views.crear_compra, name='crear_compra'),
    path('login/', views.CustomLoginView.as_view(), name='login'), 
    path('mesas/', lista_mesas, name='lista_mesas'),
    path('mesas/crear/', crear_mesa, name='crear_mesa'),
    path('mesas/editar/<int:mesa_id>/', editar_mesa, name='editar_mesa'),
    path('mesas/eliminar/<int:mesa_id>/', eliminar_mesa, name='eliminar_mesa'),
]
