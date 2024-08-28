from django.urls import path, include
from .views import CustomLoginView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    lista_mesas, 
    crear_mesa, 
    editar_mesa, 
    eliminar_mesa, 
    crear_proveedor, 
    editar_proveedor, 
    eliminar_proveedor,
    modificar_pedido,
    eliminar_pedido,
    crear_pago,
    modificar_pago,
    eliminar_pago,
    crear_reserva,
    modificar_reserva,
    eliminar_reserva,
    editar_compra,
    eliminar_compra
)

urlpatterns =[
    
    
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('', views.home, name='home'),
    
    # Pedido 
    path('pedido/crear/<int:mesa_id>/', views.crear_pedido, name='crear_pedido'),
    path('pedido/modificar/<int:pedido_id>/', views.modificar_pedido, name='modificar_pedido'),
    path('pedido/eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    
    # Pago 
    path('pago/crear/<int:pedido_id>/', views.crear_pago, name='crear_pago'),
    path('pago/modificar/<int:pago_id>/', views.modificar_pago, name='modificar_pago'),
    path('pago/eliminar/<int:pago_id>/', views.eliminar_pago, name='eliminar_pago'),

    # Reserva 
    path('reservas/', views.reservas, name='reservas'),
    path('reserva/crear/', views.crear_reserva, name='crear_reserva'),
    path('reserva/modificar/<int:reserva_id>/', views.modificar_reserva, name='modificar_reserva'),
    path('reserva/eliminar/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
    
    # Inventario 
    path('inventario/', views.inventario, name='inventario'),
    path('inventario/crear/', views.crear_inventario, name='crear_inventario'),
    path('inventario/editar/<int:pk>/', views.editar_inventario, name='editar_inventario'),
    path('inventario/eliminar/<int:pk>/', views.eliminar_inventario, name='eliminar_inventario'),
    
    # Proveedor 
    path('proveedores/', views.proveedores, name='proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    
    # Compra 
    path('compras/', views.compras, name='compras'),
    path('compra/crear/', views.crear_compra, name='crear_compra'),
    path('compra/editar/<int:compra_id>/', views.editar_compra, name='editar_compra'),
    path('compra/eliminar/<int:compra_id>/', views.eliminar_compra, name='eliminar_compra'),
    
    # Mesa 
    path('mesas/crear/', views.crear_mesa, name='crear_mesa'),
    path('mesas/', views.lista_mesas, name='lista_mesas'),
    path('mesas/eliminar/<int:mesa_id>/', views.eliminar_mesa, name='eliminar_mesa'),
    path('mesas/editar/<int:pk>/', views.editar_mesa, name='editar_mesa'),
    path('mesas/crear-reserva/<int:mesa_id>/', views.crear_reserva, name='crear_reserva'),
    path('mesas/crear-pedido/<int:mesa_id>/', views.crear_pedido, name='crear_pedido'),
    
    # Caja 
    path('caja/abrir/', views.abrir_caja, name='abrir_caja'),
    path('caja/cerrar/<int:caja_id>/', views.cerrar_caja, name='cerrar_caja'),
    path('caja/registrar_pago/<int:pedido_id>/', views.registrar_pago, name='registrar_pago'),
    path('caja/consulta/<int:caja_id>/', views.consulta_caja, name='consulta_caja'),
    
    #pagina cliente.
    path('cliente/', views.cliente, name='cliente'),
    
    
    #menu "Platos"
    path('menu/crear/', views.crear_menu, name='crear_menu'),
    ]
