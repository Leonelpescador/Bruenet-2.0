# Generated by Django 5.1 on 2024-08-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_proveedor_contacto_proveedor_contact_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='archivo_documentacion',
            field=models.FileField(blank=True, null=True, upload_to='documentos/'),
        ),
        migrations.AddField(
            model_name='compra',
            name='detalle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='tiene_documentacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
