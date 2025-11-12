from rest_framework import serializers
from .models import *

class AutorSerializer(serializers.ModelSerializer):

    # Indicamos que saque los datos de Autor e incluya todos los campos a la hora de Serializar
    class Meta:
        model = Autor
        fields = '__all__'

class ReseniaSerializer(serializers.ModelSerializer):

    # Indicamos que saque los datos de Resenia e incluya todos los campos a la hora de Serializar
    class Meta:
        model = Resenia
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    # Definimos un campo que se calcula usando una función, el nombre de esta función es get_nombreAtributo
    recent_reviews = serializers.SerializerMethodField()
    nombre_autor = serializers.ReadOnlyField(source='autor.nombre')

    # Función para calcular el atributo definido previamente, se le pasa el obj que es el objeto que se serializa
    def get_recent_reviews(self, obj):
        # Obtenemos las reseñas del objeto serializado (Libro) y las ordenamos de manera descendente y mostramos los 5 primeros
        reviews = obj.resenas.order_by('-fecha')[:5]
        # Retornamos las Reseñas del libro, indicamos que es una coleccion de objetos (many=True) y las convertimos a un formato para serializar (.data)
        return ReseniaSerializer(reviews, many=True).data

    # Indicamos que saque los datos de Libro e incluya todos los campos a la hora de Serializar
    class Meta:
        model = Libro
        fields = '__all__'
