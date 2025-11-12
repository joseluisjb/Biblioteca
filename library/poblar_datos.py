
from datetime import date
from library.models import Autor, Libro, Resenia

Autor.objects.all().delete()
Libro.objects.all().delete()
Resenia.objects.all().delete()

# Datos generados usando IA

# --- AUTORES ---
autores = [
    Autor.objects.create(nombre="Gabriel García Márquez", nacionalidad="Colombia"),
    Autor.objects.create(nombre="Julio Cortázar", nacionalidad="Argentina"),
    Autor.objects.create(nombre="Isabel Allende", nacionalidad="Chile"),
    Autor.objects.create(nombre="Mario Vargas Llosa", nacionalidad="Perú"),
    Autor.objects.create(nombre="Jorge Luis Borges", nacionalidad="Argentina"),
    Autor.objects.create(nombre="Laura Restrepo", nacionalidad="Colombia"),
    Autor.objects.create(nombre="Pablo Neruda", nacionalidad="Chile"),
    Autor.objects.create(nombre="Carlos Fuentes", nacionalidad="México"),
    Autor.objects.create(nombre="Juan Rulfo", nacionalidad="México"),
    Autor.objects.create(nombre="Ernesto Sábato", nacionalidad="Argentina"),
]

# --- LIBROS ---
libros = [
    Libro.objects.create(
        titulo="Cien años de soledad",
        autor=autores[0],
        fecha_publicacion=date(1967, 6, 5),
        resumen="Una historia épica sobre la familia Buendía en Macondo."
    ),
    Libro.objects.create(
        titulo="El amor en los tiempos del cólera",
        autor=autores[0],
        fecha_publicacion=date(1985, 3, 5),
        resumen="Una historia de amor que trasciende el tiempo."
    ),
    Libro.objects.create(
        titulo="Rayuela",
        autor=autores[1],
        fecha_publicacion=date(1963, 7, 28),
        resumen="Una novela experimental que desafía las reglas narrativas."
    ),
    Libro.objects.create(
        titulo="La casa de los espíritus",
        autor=autores[2],
        fecha_publicacion=date(1982, 1, 1),
        resumen="La historia de varias generaciones de la familia Trueba."
    ),
    Libro.objects.create(
        titulo="Conversación en La Catedral",
        autor=autores[3],
        fecha_publicacion=date(1969, 5, 1),
        resumen="Una exploración profunda del poder y la corrupción en Perú."
    ),
    Libro.objects.create(
        titulo="El Aleph",
        autor=autores[4],
        fecha_publicacion=date(1945, 9, 1),
        resumen="Relatos que exploran lo infinito, lo simbólico y lo fantástico."
    ),
    Libro.objects.create(
        titulo="Delirio",
        autor=autores[5],
        fecha_publicacion=date(2004, 2, 10),
        resumen="Una historia de locura, amor y violencia en Bogotá."
    ),
    Libro.objects.create(
        titulo="Veinte poemas de amor y una canción desesperada",
        autor=autores[6],
        fecha_publicacion=date(1924, 6, 20),
        resumen="Una de las obras más famosas de la poesía latinoamericana."
    ),
    Libro.objects.create(
        titulo="La región más transparente",
        autor=autores[7],
        fecha_publicacion=date(1958, 8, 5),
        resumen="Un retrato crítico de la sociedad mexicana moderna."
    ),
    Libro.objects.create(
        titulo="Pedro Páramo",
        autor=autores[8],
        fecha_publicacion=date(1955, 3, 2),
        resumen="Un viaje onírico al pueblo de Comala, entre vivos y muertos."
    ),
    Libro.objects.create(
        titulo="Sobre héroes y tumbas",
        autor=autores[9],
        fecha_publicacion=date(1961, 11, 1),
        resumen="Una profunda reflexión sobre la historia y la identidad argentina."
    ),
    Libro.objects.create(
        titulo="El otoño del patriarca",
        autor=autores[0],
        fecha_publicacion=date(1975, 10, 10),
        resumen="Una exploración poética del poder absoluto en un dictador caribeño."
    ),
    Libro.objects.create(
        titulo="Memoria de mis putas tristes",
        autor=autores[0],
        fecha_publicacion=date(2004, 10, 20),
        resumen="La historia de un hombre que descubre el amor a los 90 años."
    ),
]

# --- RESEÑAS ---
resenas = [
    Resenia.objects.create(libro=libros[0], texto="Una obra maestra del realismo mágico.", calificacion=5),
    Resenia.objects.create(libro=libros[1], texto="Una historia de amor eterna.", calificacion=4),
    Resenia.objects.create(libro=libros[2], texto="Una estructura narrativa fascinante y única.", calificacion=5),
    Resenia.objects.create(libro=libros[3], texto="Emotiva y llena de simbolismo.", calificacion=5),
    Resenia.objects.create(libro=libros[4], texto="Un retrato profundo de la política peruana.", calificacion=4),
    Resenia.objects.create(libro=libros[5], texto="Filosófico y enigmático. Imprescindible.", calificacion=5),
    Resenia.objects.create(libro=libros[6], texto="Refleja la locura del país y del alma humana.", calificacion=4),
    Resenia.objects.create(libro=libros[7], texto="Romántico y desesperado, de una belleza enorme.", calificacion=5),
    Resenia.objects.create(libro=libros[8], texto="Crítica aguda de la alta sociedad mexicana.", calificacion=4),
    Resenia.objects.create(libro=libros[9], texto="Misterioso, breve y poderoso.", calificacion=5),
    Resenia.objects.create(libro=libros[10], texto="Una novela intensa y simbólica.", calificacion=4),
    Resenia.objects.create(libro=libros[11], texto="Denso, poético, difícil pero brillante.", calificacion=5),
    Resenia.objects.create(libro=libros[12], texto="Triste y nostálgico, con la prosa única de Gabo.", calificacion=5),
]
