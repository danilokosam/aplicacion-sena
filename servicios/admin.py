from django.contrib import admin
from servicios.models import *

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Compra)
admin.site.register(DetalleCompra)