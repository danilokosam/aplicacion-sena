from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def get_image_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.documento}.{ext}"
    return f"usuario/usuarios/{filename}"

class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=45, verbose_name="Primer Nombre", blank=True, null=True)
    segundo_nombre = models.CharField(max_length=45, verbose_name="Segundo Nombre", blank=True, null=True)
    primer_apellido = models.CharField(max_length=45, verbose_name="Primer Apellido", blank=True, null=True)
    segundo_apellido = models.CharField(max_length=45, verbose_name="Segundo Apellido", blank=True, null=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    imagen = models.ImageField(upload_to=get_image_filename, blank=True, null=True, default=r"usuarios\default-user.jpeg")
    correo = models.EmailField(max_length=50, verbose_name="Correo", default="correo@ejemplo.com")

    class TipoDocumento(models.TextChoices):
        CEDULA = 'CC', _("Cédula")
        TARJETA = 'TI', _("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA = 'CE', _("Cédula de Extrangería")
    
    tipo_documento = models.CharField(max_length=2, choices=TipoDocumento.choices, verbose_name="Tipo de Documento")
    documento = models.PositiveIntegerField(verbose_name="Documento", unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    estado = models.BooleanField(default=True)

    def clean(self):
        if self.primer_nombre:
            self.primer_nombre = self.primer_nombre.title()
        if User.objects.filter(username=self.user.username).exists() and self.user.pk is None:
            raise ValidationError("El nombre de usuario ya existe.")

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"

    class Meta:
        verbose_name_plural = "Usuarios"

    @property
    def full_name(self):
        names = [self.primer_nombre, self.segundo_nombre, self.primer_apellido, self.segundo_apellido]
        return ' '.join(filter(None, names))

    def usuario_activo(self):
        if self.estado:
            return Usuario.objects.filter(pk=self.pk, estado=True)
        return Usuario.objects.none()
