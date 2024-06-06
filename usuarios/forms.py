from django import forms
from django.forms import widgets
from usuarios.models import Usuario


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"  # <-- Con esto nos trae todos los campos de esa tabla
        # exclude = ["estado"] # <-- Para excluir un campo
        widgets = {
            "fecha_nacimiento": widgets.DateInput(attrs={"type": "date"}, format="%Y-%m-%d")
        }
