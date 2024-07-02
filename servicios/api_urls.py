from django.urls import path
from . import api_views

urlpatterns = [
    path("servicios/", api_views.servicio_list,name="api_servicio_list")
]
