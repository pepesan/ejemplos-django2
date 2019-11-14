from django.contrib import admin

# Register your models here.
from .models import Genre, Language, Author, Book, BookInstance, Libro, Genero, Autor
admin.site.register(Libro)
admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)

