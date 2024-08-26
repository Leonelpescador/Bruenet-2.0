from django.urls import path
from .views import CustomLoginView
from . import views

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
    path('compras/', views.compras, name='compras'),
    path('compra/crear/', views.crear_compra, name='crear_compra'),
    path('login/', views.CustomLoginView.as_view(), name='login'), 
]
