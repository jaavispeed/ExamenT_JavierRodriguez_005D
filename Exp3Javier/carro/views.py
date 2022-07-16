from django.shortcuts import render

from .carro import Carro

from core.models import Producto

from pedidos.models import LineaPedido

from django.shortcuts import redirect


def agregar_producto(request, idProducto):
    carro=Carro(request)

    producto=Producto.objects.get(idProducto=idProducto)


    carro.agregar(producto=producto)

    return redirect("listadoproductos")

def eliminar_producto(request, idProducto):
    carro=Carro(request)

    producto=Producto.objects.get(idProducto=idProducto)

    carro.eliminar(producto=producto)

    return redirect("listadoproductos")


def restar_producto(request, idProducto):
    carro=Carro(request)

    producto=Producto.objects.get(idProducto=idProducto)

    carro.restar_producto(producto=producto)

    return redirect("listadoproductos")

def limpiar_carro(request, idProducto):
    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("listadoproductos")
# Create your views here.
