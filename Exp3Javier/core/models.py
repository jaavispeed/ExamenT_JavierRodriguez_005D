from django.db import models

# Create your models here.


#Modelo para clientes y producto.


class Producto (models.Model): 
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombreProducto= models.CharField(max_length=50, verbose_name='Nombre de Producto')
    imagen = models.ImageField(upload_to="productos", null=True)
    precio = models.IntegerField(verbose_name='precio', null=True)
    cantidad = models.IntegerField(verbose_name='cantidad', null=True)
    estado= models.CharField(max_length=50, verbose_name='Estado', null=True)

    def __str__(self):
        return self.nombreProducto


class Cliente(models.Model):
    rut= models.CharField(max_length=9, primary_key=True, verbose_name='Rut')
    nombrec= models.CharField(max_length=20, verbose_name='Nombre Cliente')
    correo= models.CharField(max_length=30, verbose_name='Correo Cliente', null=True)
    direccion= models.CharField(max_length=20, verbose_name='Direccion Cliente', null=True)
    telefono= models.IntegerField(verbose_name='Telefono Cliente', null=True)
    producto= models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut
