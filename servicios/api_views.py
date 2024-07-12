from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from servicios.models import Servicio
from servicios.serializers import ServicioSerializer


@api_view(['GET', 'POST'])
def servicio_list(request):
    if request.method == 'GET':
        servicios = Servicio.objects.all()
        serializer = ServicioSerializer(servicios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def servicio_detail(request, id):
    try:
        servicio = Servicio.objects.delete(id=id)
    except Servicio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        serializer = ServicioSerializer(servicio)
        return Response(serializer.data)