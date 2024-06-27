from django.shortcuts import render


def index_admin(request):
    titulo = "Inicio"
    contexto = {
        'titulo': titulo
    }
    return render(request, 'index-admin.html', contexto)


def productos(request):
    return render(request, 'productos.html', {})


def inicio(request):
    return render(request, 'inicio.html', {})


def index(request):
    return render(request, 'index.html', {})
