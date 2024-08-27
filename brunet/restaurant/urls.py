from django.urls import path
from .views import CustomLoginView
from . import views
from .views import lista_mesas, crear_mesa, editar_mesa, eliminar_mesa, crear_proveedor, editar_proveedor, eliminar_proveedor

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('', views.home, name='home'),
    
    path('pedido/crear/<int:mesa_id>/', views.crear_pedido, name='crear_pedido'),
    path('pago/crear/<int:pedido_id>/', views.crear_pago, name='crear_pago'),
   
    path('reservas/', views.reservas, name='reservas'),
    path('reserva/crear/', views.crear_reserva, name='crear_reserva'),
    
    path('inventario/', views.inventario, name='inventario'),
    path('inventario/crear/', views.crear_inventario, name='crear_inventario'),
    path('inventario/editar/<int:pk>/', views.editar_inventario, name='editar_inventario'),
    path('inventario/eliminar/<int:pk>/', views.eliminar_inventario, name='eliminar_inventario'),
    
    path('proveedores/', views.proveedores, name='proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    
    path('compras/', views.compras, name='compras'),
    path('compra/crear/', views.crear_compra, name='crear_compra'),
    
    
    path('mesas/crear/', views.crear_mesa, name='crear_mesa'),
    path('mesas/', views.lista_mesas, name='lista_mesas'),
    path('mesas/eliminar/<int:mesa_id>/', views.eliminar_mesa, name='eliminar_mesa'),
    path('mesas/editar/<int:pk>/', views.editar_mesa, name='editar_mesa'),
    path('mesas/crear-reserva/<int:mesa_id>/', views.crear_reserva, name='crear_reserva'),
    path('mesas/crear-pedido/<int:mesa_id>/', views.crear_pedido, name='crear_pedido'),
    
    path('caja/abrir/', views.abrir_caja, name='abrir_caja'),
    path('caja/cerrar/<int:caja_id>/', views.cerrar_caja, name='cerrar_caja'),
    path('caja/registrar_pago/<int:pedido_id>/', views.registrar_pago, name='registrar_pago'),
    path('caja/consulta/<int:caja_id>/', views.consulta_caja, name='consulta_caja'),
    
    
]
