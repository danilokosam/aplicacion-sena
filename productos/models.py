from django.db import models

def get_image_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.nombre}.{ext}"
    return f"productos/productos/{filename}"
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
    imagen = models.ImageField(upload_to=get_image_filename, null=True, blank=True)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    