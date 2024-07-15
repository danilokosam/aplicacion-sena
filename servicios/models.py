from django.db import models
from usuarios.models import Usuario

def get_image_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.nombre}.{ext}"
    return f"servicios/servicios/{filename}"

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=45, verbose_name="Nombre")
    descripcion = models.CharField(max_length=200,verbose_name="Descripción")
    imagen = models.ImageField(upload_to=get_image_filename, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Compra(models.Model):
    fecha = models.DateField(verbose_name="Fecha")
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Compra #" + str(self.id)
    
class DetalleCompra(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return "Detalle de compra # " + str(self.compra.id) + " para el servicio " + str(self.servicio.nombre)
    
opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "servicio"],
    [3, "felicitaciones"],
    [4, "otro"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    teléfono = models.CharField(max_length=12)
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    aviso = models.BooleanField()

    def __str__(self):
        return self.nombre
       
