from django import forms
from django.forms import ModelForm, ModelChoiceField, widgets
from servicios.models import Servicio, Contacto


class ServicioForm(ModelForm):

    class Meta:
        model = Servicio
        fields = "__all__"
        exclude = ["estado"]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }


class ServicioEditarForm(ModelForm):

    class Meta:
        model = Servicio
        fields = "__all__"
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class contactoforms(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'