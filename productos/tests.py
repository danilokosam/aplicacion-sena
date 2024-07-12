from django.test import TestCase
from .models import TipoProducto, Producto

class TipoProductoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        TipoProducto.objects.create(nombre='Electrónica')

    def test_nombre_label(self):
        tipo_producto = TipoProducto.objects.get(id=1)
        field_label = tipo_producto._meta.get_field('nombre').verbose_name
        self.assertEqual(field_label, 'nombre')

    def test_nombre_max_length(self):
        tipo_producto = TipoProducto.objects.get(id=1)
        max_length = tipo_producto._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 50)

    def test_object_name_is_nombre(self):
        tipo_producto = TipoProducto.objects.get(id=1)
        expected_object_name = f'{tipo_producto.nombre}'
        self.assertEqual(str(tipo_producto), expected_object_name)


class ProductoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        tipo_producto = TipoProducto.objects.create(nombre='Electrónica')
        Producto.objects.create(
            nombre='Laptop',
            precio=1500,
            descripcion='Una laptop de alta calidad.',
            marca=tipo_producto,
            estado=True
        )

    def test_nombre_label(self):
        producto = Producto.objects.get(id=1)
        field_label = producto._meta.get_field('nombre').verbose_name
        self.assertEqual(field_label, 'nombre')

    def test_precio_label(self):
        producto = Producto.objects.get(id=1)
        field_label = producto._meta.get_field('precio').verbose_name
        self.assertEqual(field_label, 'precio')

    def test_descripcion_label(self):
        producto = Producto.objects.get(id=1)
        field_label = producto._meta.get_field('descripcion').verbose_name
        self.assertEqual(field_label, 'descripcion')

    def test_marca_label(self):
        producto = Producto.objects.get(id=1)
        field_label = producto._meta.get_field('marca').verbose_name
        self.assertEqual(field_label, 'marca')

    def test_imagen_label(self):
        producto = Producto.objects.get(id=1)
        field_label = producto._meta.get_field('imagen').verbose_name
        self.assertEqual(field_label, 'imagen')

    def test_estado_label(self):
        producto = Producto.objects.get(id=1)
        field_label = producto._meta.get_field('estado').verbose_name
        self.assertEqual(field_label, 'estado')

    def test_nombre_max_length(self):
        producto = Producto.objects.get(id=1)
        max_length = producto._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 50)

    def test_object_name_is_nombre(self):
        producto = Producto.objects.get(id=1)
        expected_object_name = f'{producto.nombre}'
        self.assertEqual(str(producto), expected_object_name)

    def test_precio_default_value(self):
        producto = Producto.objects.get(id=1)
        self.assertEqual(producto.precio, 1500)

    def test_descripcion_content(self):
        producto = Producto.objects.get(id=1)
        expected_descripcion = 'Una laptop de alta calidad.'
        self.assertEqual(producto.descripcion, expected_descripcion)

    def test_estado_default_value(self):
        producto = Producto.objects.get(id=1)
        self.assertTrue(producto.estado)
