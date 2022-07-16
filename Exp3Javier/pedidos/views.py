from django.shortcuts import redirect, render

from pedidos.models import LineaPedido, Pedido, User
from carro.carro import Carro
from django.contrib import messages

from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import send_mail

# Create your views here.

def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)



    messages.success(request, "La compra se ha realizado correctamente!")
    return redirect("/")



