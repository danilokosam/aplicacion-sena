from django import forms
from django.forms import ModelForm
from productos.models import Producto, TipoProducto

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"
        exclude = ["estado"]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class ProductoEditarForm(ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }