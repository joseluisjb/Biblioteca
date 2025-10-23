
from datetime import date
from library.models import Autor, Libro, Resenia

# Crear autores
autor1 = Autor.objects.create(nombre="Gabriel García Márquez", nacionalidad="Colombia")
autor2 = Autor.objects.create(nombre="Julio Cortázar", nacionalidad="Argentina")
autor3 = Autor.objects.create(nombre="Isabel Allende", nacionalidad="Chile")

# Crear libros
libro1 = Libro.objects.create(
    titulo="Cien años de soledad",
    autor=autor1,
    fecha_publicacion=date(1967, 6, 5),
    resumen="Una historia épica sobre la familia Buendía en Macondo."
)

libro2 = Libro.objects.create(
    titulo="El amor en los tiempos del cólera",
    autor=autor1,
    fecha_publicacion=date(1985, 3, 5),
    resumen="Una historia de amor que trasciende el tiempo."
)

libro3 = Libro.objects.create(
    titulo="Rayuela",
    autor=autor2,
    fecha_publicacion=date(1963, 7, 28),
    resumen="Una novela experimental que desafía las reglas narrativas."
)

libro4 = Libro.objects.create(
    titulo="La casa de los espíritus",
    autor=autor3,
    fecha_publicacion=date(1982, 1, 1),
    resumen="La historia de varias generaciones de la familia Trueba."
)

# Crear reseñas
Resenia.objects.create(libro=libro1, texto="Una obra maestra del realismo mágico.", calificacion=5)
Resenia.objects.create(libro=libro3, texto="Una estructura narrativa fascinante y única.", calificacion=4)
Resenia.objects.create(libro=libro4, texto="Emotiva y llena de simbolismo.", calificacion=5)
Resenia.objects.create(libro=libro2, texto="Una historia de amor eterna.", calificacion=4)