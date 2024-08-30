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
    crear_pedido, 
    modificar_pedido,
    eliminar_pedido,
    crear_pago,
    modificar_pago,
    eliminar_pago,
    crear_reserva,
    modificar_reserva,
    eliminar_reserva,
    editar_compra,
    eliminar_compra,
    proveedores, 
    editar_proveedor,
    eliminar_proveedor,
    crear_compra,  
    compras,
    editar_compra,
    eliminar_compra,
    obtener_precio_plato
)

urlpatterns =[
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('', views.home, name='home'),
    
    # Clientes
    path('cliente/', views.cliente, name='cliente'),
    
    
    #pedidos
    path('pedido/', views.pedidos_activos, name='pedidos_activos'),
    path('pedido/crear/<int:mesa_id>/', views.crear_pedido, name='crear_pedido'),
    path('pedido/modificar/<int:pedido_id>/', views.modificar_pedido, name='modificar_pedido'),
    path('pedido/eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('obtener_precio_plato/', obtener_precio_plato, name='obtener_precio_plato'),


    # Pago 
    path('pago/crear/<int:pedido_id>/', views.crear_pago, name='crear_pago'),
    path('pago/modificar/<int:pago_id>/', views.modificar_pago, name='modificar_pago'),
    path('pago/eliminar/<int:pago_id>/', views.eliminar_pago, name='eliminar_pago'),


    # Reserva 
    path('reserva/crear/', views.crear_reserva, name='crear_reserva'),
    path('reserva/modificar/<int:reserva_id>/', views.modificar_reserva, name='modificar_reserva'),
    path('reserva/eliminar/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
    path('reservas/', views.reservas, name='reservas'),


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
    path('compra/', views.compras, name='compras'),
    path('compra/crear/', views.crear_compra, name='crear_compra'),  
    path('compra/editar/<int:pk>/', views.editar_compra, name='editar_compra'),
    path('compra/eliminar/<int:pk>/', views.eliminar_compra, name='eliminar_compra'),
    
    
    # Mesa 
    path('mesa/crear/', views.crear_mesa, name='crear_mesa'),
    path('mesa/', views.lista_mesas, name='lista_mesas'),
    path('mesa/eliminar/<int:mesa_id>/', views.eliminar_mesa, name='eliminar_mesa'),
    path('mesa/editar/<int:pk>/', views.editar_mesa, name='editar_mesa'),
    
    
    # Caja 
    path('caja/apertura/', views.apertura_caja, name='apertura_caja'),
    path('caja/consulta/<int:caja_id>/', views.consulta_caja, name='consulta_caja'),
    path('caja/cierre/', views.cierre_caja, name='cierre_caja'),
    path('caja/registrar_pago/<int:pedido_id>/', views.registrar_pago, name='registrar_pago'),
    
    
    # Menu "Platos"
    path('menu/listar/', views.listar_menu, name='listar_menu'),
    path('menu/crear/', views.crear_menu, name='crear_menu'),
    path('menu/editar/<int:menu_id>/', views.editar_menu, name='editar_menu'),
    path('menu/eliminar/<int:menu_id>/', views.eliminar_menu, name='eliminar_menu'),
    path('menu/cambiar-disponibilidad/<int:menu_id>/', views.cambiar_disponibilidad_menu, name='cambiar_disponibilidad_menu'),
    
    
    # Caja
    path('caja/pago/crear/', views.crear_pago, name='crear_pago'),
    path('caja/pago/modificar/<int:pago_id>/', views.modificar_pago, name='modificar_pago'),
    path('caja/pago/eliminar/<int:pago_id>/', views.eliminar_pago, name='eliminar_pago'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
