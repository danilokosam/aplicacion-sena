from django.contrib import admin
from django.urls import path

from aplicacion.views import contacto_list_view, index_admin
from servicios.views import *

urlpatterns = [
    path("servicios/", servicio_list_view, name="servicios-listar"),
    path("servicio/<int:id>/", servicio_list_view, name="servicios-editar"),
    path('contacto/eliminar/<int:id>/', contacto_delete_view, name='contacto-eliminar'),
    path("servicio/eliminar/<int:id>/", servicio_delete_view, name="servicio-eliminar"),
    path("contacto/listar/", contacto_list_view, name="contacto-listar"),
    path("contacto/", contacto, name="contacto"),
]
