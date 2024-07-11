# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Producto, TipoProducto
# from productos.serialiazers import ProductoSerializer, TipoProductoSerializer


# @api_view(['GET', 'POST'])
# def producto_list(request):
#     if request.method == 'GET':
#         producto = Producto.objects.all()
#         serializer = ProductoSerializer(producto, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
