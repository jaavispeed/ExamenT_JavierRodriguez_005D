# Generated by Django 4.0.5 on 2022-07-15 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_producto_cantidad'),
        ('pedidos', '0004_alter_lineapedido_cantidad_alter_lineapedido_pedido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineapedido',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='lineapedido',
            name='producto',
        ),
        migrations.AddField(
            model_name='lineapedido',
            name='pedido_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido'),
        ),
        migrations.AddField(
            model_name='lineapedido',
            name='producto_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
        ),
    ]
