# Generated by Django 5.0.6 on 2024-07-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_servicio_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='servicios'),
        ),
    ]
