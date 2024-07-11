from django.urls import path,include
from rest_framework import routers
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista-productos'),
    path('productos-admin/', views.producto_list_view, name='productos-listar'),
    path('productos/<int:id>/', views.producto_list_view, name='productos-editar'),
    path('productos/eliminar/<int:id>/', views.producto_delete_view, name='producto-eliminar'),
]