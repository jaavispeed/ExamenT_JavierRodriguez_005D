from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from core.models import Producto
from django.db.models import F, Sum, IntegerField
# Create your models here.

User=get_user_model()

class Pedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def total (self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=IntegerField())
        )["total"]

    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='Pedidos'
        ordering=['id']

class LineaPedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE,null=True)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE,null=True)
    cantidad=models.IntegerField(default=1,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    estado=models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto}'
    
    class Meta:
        db_table='lineapedidos'
        verbose_name='Linea Pedido'
        verbose_name_plural='Lineas Pedidos'
        ordering=['id']