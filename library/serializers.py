from rest_framework import serializers

class LibroSerializer(serializers.ModelSerializer):
    recent_reviews = serializers.SerializerMethodField()
    author_name = serializers.ReadOnlyField(source='autor.nombre')

    def get_recent_reviews(self, obj):
        reviews = obj.review_set.order_by('-date')[:5]
        return ReseniaSerializer(reviews, many=True).data

class AutorSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='autor.nombre')
    nacionality = serializers.ReadOnlyField(source='autor.nacionalidad')

class ReseniaSerializer(serializers.ModelSerializer):
    libro = serializers.ReadOnlyField(source='resenia.libro')
    texto = serializers.ReadOnlyField(source='resenia.texto')
    calificacion = serializers.ReadOnlyField(source='resenia.calificacion')
    fecha = serializers.ReadOnlyField(source='resenia.fecha')
    rating = serializers.ReadOnlyField(source='resenia.rating')