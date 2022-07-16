from django.urls import path
from rest_cliente.views import lista_clientes,detalle_clientes


urlpatterns = [
    path('lista_clientes', lista_clientes, name="lista_clientes"),
    path('detalle_clientes/<id>', detalle_clientes, name="detalle_clientes"),

]