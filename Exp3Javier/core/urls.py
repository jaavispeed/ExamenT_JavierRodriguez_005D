from xml.etree.ElementInclude import include
from django.urls import path



from .views import miscompras, index, somos, galeria, formulariocontacto, formularioregistro, clientesadmin, RegistrarClientes, eliminarCliente, editarCliente,modificarClientes,productosadmin,RegistrarProductos,editarProducto,modificarProducto,eliminarProducto, registro, listadoproductos
from django import urls
from django.contrib import admin


urlpatterns =[
        path('', index, name="index"),
        path('somos/', somos, name="somos"),
        path('galeria/', galeria, name="galeria"),
        path('formulariocontacto/', formulariocontacto, name="formulariocontacto"),
        path('formularioregistro/', formularioregistro, name="formularioregistro"),
        path('clientesadmin/', clientesadmin, name="clientesadmin"),
        path('RegistrarClientes/', RegistrarClientes, name="RegistrarClientes"),
        path('editarCliente/<id>', editarCliente, name="editarCliente"),
        path('modificarClientes/',modificarClientes, name="modificarClientes"),
        path('eliminarCliente/<id>', eliminarCliente, name="eliminarCliente"),
        path('productosadmin/', productosadmin, name="productosadmin"),
        path('RegistrarProductos/', RegistrarProductos, name="RegistrarProductos"),
        path('editarProducto/<id>', editarProducto, name="editarProducto"),
        path('modificarProducto/', modificarProducto, name="modificarProducto"),
        path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
        path('registro/', registro, name="registro"),
        path('listadoproductos/', listadoproductos, name="listadoproductos"),
        path('miscompras/', miscompras, name="miscompras"),
        
]