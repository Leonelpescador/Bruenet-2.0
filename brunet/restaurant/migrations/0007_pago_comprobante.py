# Generated by Django 5.1 on 2024-08-30 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_detallepedido_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='comprobante',
            field=models.FileField(blank=True, null=True, upload_to='comprobantes/'),
        ),
    ]
