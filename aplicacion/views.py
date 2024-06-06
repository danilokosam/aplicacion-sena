from django.shortcuts import render


def productos(request):
    return render(request, 'productos.html', {})


def inicio(request):
    return render(request, 'inicio.html', {})


def index(request):
    return render(request, 'index.html', {})
