
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg

class AutorModelViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    # Definimos los mecanismos de filtrado y ordenamiento
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    #filterset_fields = ['nombre', 'nacionalidad'] - Filterset_fields busca el nombre exacto

    # Campos por los que se pueden ordenar los Autores, usando /?ordering=nombre y /?ordering=nacionalidad
    ordering_fields = ['nombre', 'nacionalidad']

    # Sobreescribimos el conjunto que se mostrará, filtrando solo los que coinciden parcialmente con el parámetro nombre
    def get_queryset(self):
        queryset = Autor.objects.all()
        nombre_autor = self.request.query_params.get('nombre')
        if nombre_autor:
            queryset = queryset.filter(nombre__icontains=nombre_autor)
        return queryset

class LibroModelViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    # Definimos los mecanismos de filtrado y ordenamiento
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Definimos campos para filtrar usando el ID del autor y la fecha de publicación del libro.
    filterset_fields = ['autor', 'fecha_publicacion']
    # Definimos campos para ordenar usando el título del libro y la fecha de publicación del libro
    ordering_fields = ['titulo', 'fecha_publicacion']

    # Si se usa el parámetro /?reciente=true se mostrarán en orden descendente los primeros 10 Libros por fecha de publicación
    def get_queryset(self):
        if self.request.query_params.get('reciente'):
            return Libro.objects.order_by('-fecha_publicacion')[:10]
        return Libro.objects.all()
    
    # Definimos un endpoint personalizado denominado resumen
    # detail=True indica que se le debe especificar la llave primaria del objeto Libro y solo funciona para métodos get
    # su endpoint es /<id_libro>/resumen/
    @action(detail=True, methods=['get'])
    def resumen(self, request, pk=None):
        libro = self.get_object()
        resumen = f"{libro.titulo} - {libro.autor} - Publicado: {libro.fecha_publicacion}"
        return Response({'resumen': resumen})
    
    # Definimos otro endpoint personalizado que devuelve el promedio de calificaciones de un libro tomando su ID
    @action(detail=True, methods=['get'])
    def rating_promedio(self, request, pk=None):
        libro = self.get_object()
        promedio = libro.resenas.aggregate(rating_promedio=Avg('calificacion'))['rating_promedio']
        return Response({'rating_promedio': promedio})

class ReseniaModelViewSet(viewsets.ModelViewSet):
    queryset = Resenia.objects.all()
    serializer_class = ReseniaSerializer
    # Definimos los mecanismos de filtrado y ordenamiento
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Definimos campos para filtrar usando la calificación de la Reseña
    filterset_fields = ['calificacion']
    # Definimos campos para ordenar usando la calificación de la Reseña
    ordering_fields = ['calificacion']

    # Cuando se usa el parámetro /?reciente=true en el endpoint devuelve las reseñas ordenadas en forma descendente
    def get_queryset(self):
        if self.request.query_params.get('reciente'):
            return Resenia.objects.order_by('-fecha')
        return Resenia.objects.all()