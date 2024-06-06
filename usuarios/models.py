from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=45, verbose_name=_("Nombre"))
    apellido = models.CharField(max_length=45, verbose_name=_("Apellido"))
    telefono = models.CharField(max_length=10, verbose_name=_("Teléfono"))
    fecha_nacimiento = models.DateField(verbose_name=_("Fecha de Nacimiento"))

    class TipoDocumento(models.TextChoices):
        CEDULA = "CC", _("Cédula")
        TARJETA = "TI", _("Tarjeta de Identidad")
        PASAPORTE = "PP", _("Pasaporte")

    tipo_documento = models.CharField(
        max_length=2,
        choices=TipoDocumento.choices,
        verbose_name=_("Tipo de Documento")
    )
    documento = models.PositiveIntegerField(
        verbose_name=_("Documento"),
        unique=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
