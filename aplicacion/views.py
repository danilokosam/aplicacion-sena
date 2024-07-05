from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

from servicios.models import Servicio

@login_required
def index_admin(request):
    titulo = "Inicio"
    contexto = {
        'titulo': titulo
    }
    return render(request, 'index-admin.html', contexto)

def index_user(request):
    titulo = "Inicio"
    contexto = {
        'titulo': titulo
    }
    return render(request, 'users/index-user.html', contexto)

def productos(request):
    return render(request, 'productos.html', {})

def index(request):
    return render(request, 'index.html', {})

def logout_user(reqest):
    logout(reqest)
    return redirect('index') # <-- O dirigir a inico


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index-admin')

def serviciosuser(request):
    servicios=Servicio.objects.all()
    context={
        'servicios':servicios
    }
    return render(request, 'servicios-user.html', context)
