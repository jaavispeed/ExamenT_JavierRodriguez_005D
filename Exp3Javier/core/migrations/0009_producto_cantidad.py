# Generated by Django 4.0.5 on 2022-07-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(null=True, verbose_name='cantidad'),
        ),
    ]
