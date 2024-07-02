from django import forms
from django.forms import ModelForm, ModelChoiceField, widgets
from servicios.models import Servicio


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