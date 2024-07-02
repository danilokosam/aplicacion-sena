from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(TipoProducto, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='productos', null=True)
    
    def __str__(self):
        return self.nombre
    