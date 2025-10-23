from django.contrib import admin

from .models import Autor
from .models import Libro
from .models import Resenia

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')
    list_filter = ('nombre', 'nacionalidad')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'resumen')
    search_fields = ('titulo', 'autor')
    list_filter = ('titulo', 'fecha_publicacion')

@admin.register(Resenia)
class ReseniaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'texto', 'calificacion', 'fecha')
    search_fields = ('libro', 'calificacion')
    list_filter = ('calificacion',)