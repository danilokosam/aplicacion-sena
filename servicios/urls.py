from django.contrib import admin
from django.urls import path

from aplicacion.views import index_admin
from servicios.views import *

urlpatterns = [
    path("servicios/", servicio_list_view, name="servicios-listar"),
    path("servicio/<int:id>/", servicio_list_view, name="servicios-editar"),
    path("servicio/eliminar/<int:id>/", servicio_delete_view, name="servicio-eliminar"),
]
