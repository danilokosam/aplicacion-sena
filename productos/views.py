from django.shortcuts import render
from .models import Producto

def productos(request):
    productos = Producto.objects.all() 
    data = {
        'productos': productos  
    }
    return render(request, 'productos.html', data)