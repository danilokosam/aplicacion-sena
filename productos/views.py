from django.shortcuts import render, redirect
from productos.forms import ProductoForm, ProductoEditarForm
from rest_framework import viewsets
from .serialiazers import ProductoSerializer, TipoProductoSerializer
from .models import Producto, TipoProducto

from django.contrib import messages

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer


def lista_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'productos.html', data)

def producto_list_view(request, id=None):
    titulo = "Productos"
    
    if request.method == 'POST' and id:
        producto = Producto.objects.get(id=id)
        form = ProductoEditarForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            producto = form.save()
            messages.success(
                request, f'¡El producto se editó de forma exitosa!')
            return redirect("productos-listar")
        else:
            form = ProductoEditarForm(
                request.POST, request.FILES, instance=producto)
            messages.error(request, f'¡Error al editar producto!')
    elif request.method == 'POST':
        print(request.FILES) 
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
                form.save()
                messages.success(
                request, f'¡El producto se agregó de forma exitosa!')
                return redirect('productos-listar')
        else:
            error_messages = form.errors.as_json()
            print("Error al agregar producto:", error_messages)  # Para depuración
            messages.error(request, f'¡Error al agregar producto! Detalles: {error_messages}')
    else:
        if (id):
            producto = Producto.objects.get(id=id)
            form = ProductoEditarForm(instance=producto)
        else:
            form = ProductoForm()
    context = {
        "titulo": titulo,
        "form": form,
    }
    return render(request, 'admin/productos/productos.html', context)

def producto_delete_view(request, id):
    producto = Producto.objects.filter(id=id)
    producto.update(estado=False)
    messages.success(
        request, f'¡El producto se elimino de forma exitosa!')
    return redirect('productos-listar')