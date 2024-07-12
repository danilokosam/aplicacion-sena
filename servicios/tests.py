from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Servicio, Compra, DetalleCompra, Contacto, Usuario

class ServicioModelTest(TestCase):

    def setUp(self):
        Servicio.objects.create(nombre='Limpieza', descripcion='Servicio de limpieza general', estado=True)

    def test_str(self):
        servicio = Servicio.objects.get(nombre='Limpieza')
        self.assertEqual(str(servicio), 'Limpieza')

class CompraModelTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='juan', password='password')
        usuario = Usuario.objects.create(user=user, primer_nombre='Juan', documento=12345678, fecha_nacimiento=timezone.now().date())
        Compra.objects.create(fecha=timezone.now().date(), cliente=usuario)

    def test_str(self):
        compra = Compra.objects.get(id=1)
        self.assertTrue('Compra #' in str(compra))

class DetalleCompraModelTest(TestCase):

    def setUp(self):
        servicio = Servicio.objects.create(nombre='Limpieza', descripcion='Servicio de limpieza general', estado=True)
        user = User.objects.create(username='juan', password='password')
        usuario = Usuario.objects.create(user=user, primer_nombre='Juan', documento=12345678, fecha_nacimiento=timezone.now().date())
        compra = Compra.objects.create(fecha=timezone.now().date(), cliente=usuario)
        DetalleCompra.objects.create(servicio=servicio, compra=compra, precio=100.00)

    def test_str(self):
        detalle_compra = DetalleCompra.objects.get(id=1)
        self.assertTrue('Detalle de compra #' in str(detalle_compra))

class ContactoModelTest(TestCase):

    def setUp(self):
        Contacto.objects.create(nombre='Carlos', correo='carlos@example.com', telefono='1234567890', tipo_consulta=0, mensaje='Mensaje de prueba', aviso=True)

    def test_str(self):
        contacto = Contacto.objects.get(nombre='Carlos')
        self.assertEqual(str(contacto), 'Carlos')
