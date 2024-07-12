from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.utils import IntegrityError
from .models import Usuario
from datetime import date

class UsuarioModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.usuario = Usuario.objects.create(
            primer_nombre="Juan",
            primer_apellido="Perez",
            fecha_nacimiento=date(1990, 1, 1),
            tipo_documento="CC",
            documento=1234567890,
            user=self.user
        )

    def test_crear_usuario(self):
        self.assertTrue(isinstance(self.usuario, Usuario))
        self.assertEqual(self.usuario.__str__(), "Juan Perez")

    def test_verbose_name_plural(self):
        self.assertEqual(str(Usuario._meta.verbose_name_plural), "Usuarios")

    def test_full_name_property(self):
        self.assertEqual(self.usuario.full_name, "Juan Perez")
        self.usuario.segundo_nombre = "Carlos"
        self.usuario.segundo_apellido = "Gomez"
        self.usuario.save()
        self.assertEqual(self.usuario.full_name, "Juan Carlos Perez Gomez")

    def test_clean_method(self):
        self.usuario.primer_nombre = "juan"
        self.usuario.clean()
        self.assertEqual(self.usuario.primer_nombre, "Juan")

    def test_usuario_activo(self):
        self.assertTrue(self.usuario.usuario_activo().exists())
        self.usuario.estado = False
        self.usuario.save()
        self.assertFalse(self.usuario.usuario_activo().exists())

    def test_unique_documento(self):
        with self.assertRaises(IntegrityError):
            Usuario.objects.create(
                primer_nombre="Maria",
                primer_apellido="Lopez",
                fecha_nacimiento=date(1995, 5, 5),
                tipo_documento="CC",
                documento=1234567890,
                user=User.objects.create_user(username='testuser2', password='12345')
            )

    def test_tipo_documento_choices(self):
        self.usuario.tipo_documento = "XX"
        with self.assertRaises(ValidationError):
            self.usuario.full_clean()

    def test_image_upload(self):
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.usuario.imagen = image
        self.usuario.save()
        self.assertTrue(self.usuario.imagen.name.startswith("usuario/usuarios/"))
        self.assertTrue(self.usuario.imagen.name.endswith(".jpg"))

    def test_user_validation(self):
        with self.assertRaises(ValidationError):
            Usuario(
                primer_nombre="Test",
                primer_apellido="User",
                fecha_nacimiento=date(2000, 1, 1),
                tipo_documento="TI",
                documento=9876543210,
                user=User(username='testuser')
            ).clean()
