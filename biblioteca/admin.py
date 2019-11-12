from django.contrib import admin

# Register your models here.
from .models import Genre, Language, Author, Book, BookInstance

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)

