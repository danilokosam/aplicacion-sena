from django.shortcuts import render

from usuarios.forms import UsuarioForm

# Create your views here.


def agregarUsuario(request):
    titulo = "Usuarios"
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            print(f"{usuario.nombre} fue agregado")
    else:
        form = UsuarioForm()
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "usuarios/usuario.html", context)
