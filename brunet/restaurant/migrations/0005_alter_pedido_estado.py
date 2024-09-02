# Generated by Django 5.1 on 2024-09-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_pedido_usuario_procesando'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('preparando', 'Preparando'), ('servido', 'Servido'), ('pagado', 'Pagado')], default='pendiente', max_length=10),
        ),
    ]
