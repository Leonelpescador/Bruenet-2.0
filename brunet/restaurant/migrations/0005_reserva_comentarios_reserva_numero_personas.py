# Generated by Django 5.1 on 2024-08-29 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_compra_archivo_documentacion_compra_detalle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='comentarios',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='numero_personas',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]