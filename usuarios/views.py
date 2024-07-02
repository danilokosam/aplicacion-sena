from django.shortcuts import render, redirect
from usuarios.forms import UsuarioEditarForm, UsuarioForm
from usuarios.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from PIL import Image

def usuario_list_view(request, id=None):
    titulo = "Usuarios"

    if request.method == 'POST' and id:
        usuario = Usuario.objects.get(id=id)
        form = UsuarioEditarForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, '¡El Usuario se editó de forma exitosa!')
            return redirect("usuarios-listar")
        else:
            messages.error(request, '¡Error al editar usuario!')

    elif request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            documento = request.POST.get('documento')
            if not User.objects.filter(username=documento).exists():
                password = make_password("@" + request.POST['primer_nombre'][0] + request.POST['primer_apellido'][0] + request.POST['documento'][-4:])
                user = User.objects.create_user(
                    username=documento,
                    first_name=request.POST.get('primer_nombre'),
                    last_name=request.POST.get('primer_apellido'),
                    email=request.POST.get('correo'),
                    password=password
                )
            else:
                user = User.objects.get(username=documento)

            usuario = Usuario.objects.create(
                primer_nombre=request.POST.get('primer_nombre'),
                segundo_nombre=request.POST.get('segundo_nombre'),
                primer_apellido=request.POST.get('primer_apellido'),
                segundo_apellido=request.POST.get('segundo_apellido'),
                fecha_nacimiento=request.POST.get('fecha_nacimiento'),
                imagen=request.FILES.get('imagen'),
                correo=request.POST.get('correo'),
                tipo_documento=request.POST.get('tipo_documento'),
                documento=documento,
                user=user
            )

            if usuario.imagen:
                img = Image.open(usuario.imagen.path)
                img = img.resize((500, 500))
                img.save(usuario.imagen.path)

            usuario.save()
            messages.success(request, '¡El Usuario se agregó de forma exitosa!')
            return redirect('usuarios-listar')
        else:
            messages.error(request, '¡Error al agregar usuario!')

    else:
        if id:
            usuario = Usuario.objects.get(id=id)
            form = UsuarioEditarForm(instance=usuario)
        else:
            form = UsuarioForm()

    context = {
        "titulo": titulo,
        "form": form,
    }
    return render(request, 'admin/comunidad/usuarios.html', context)

def usuario_delete_view(request, id):
    usuario = Usuario.objects.filter(id=id)
    usuario.update(estado=False)
    return redirect('usuarios-listar')
