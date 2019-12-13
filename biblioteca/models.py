from django.db import models

# Create your models here.
from django.urls import reverse
import uuid  # Requerido por las BooksInstances
from rest_framework import serializers, viewsets

class Libro(models.Model):
    #Atributo de cada Libro, marca que es un conjunto de caracteres con un máximo de 200pk
    nombre = models.CharField(max_length=200)
    escritor= models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    generos = models.ManyToManyField('Genero', help_text="Select a genre for this book", null=True, blank=True)
    #Función de conversión a cadena del objeto
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        """Devuelve el URL a una instancia particular de
           Libro"""
        return reverse('genericas:libro-detail', args=[str(self.id)])

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id', 'nombre', 'escritor', 'generos')

class Autor(models.Model):
    nombre= models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id', 'nombre')

class Genero (models.Model):
    nombre=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre




#class ProductoSerializer(serializers.HyperlinkedModelSerializer):
class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('id', 'nombre')

class Language(models.Model):
    """
    Modelo que representa un idioma por ejemplo español
    """
    name = models.CharField(max_length=200, help_text="Introduce un nombre de idioma")
    codigo = models.CharField(max_length=6, help_text="Introduce un código de idioma")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej en el sitio de Administración)
        """
        return self.name

class Genre(models.Model):
    """Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.)."""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """Cadena que representa a la instancia particular del modelo (p. ej en
        el sitio de Administración)"""
        return self.name
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('biblioteca:genre-detail', args=[str(self.id)])

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('biblioteca:author-detail', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return '%s, %s' % (self.last_name, self.first_name)

class Book(models.Model):
    """Modelo que representa un libro (pero no un Ejemplar específico)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbninternational.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField, porque un género puede contener muchos libros y un libro puede cubrir varios géneros.
    # La clase Genre ya ha sido definida, entonces podemos especificar el objeto arriba
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        """String que representa al objeto Book"""
        return self.title

    def get_absolute_url(self):
        """Devuelve el URL a una instancia particular de
           Book"""
        return reverse('biblioteca:book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Identificativo único para este libro físico")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id, self.book.title)

class Ordenador(models.Model):
    marca= models.CharField(max_length=100)
    modelo=models.CharField(max_length=100)
    precio = models.FloatField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.marca + ": " +self.modelo


class Noticia(models.Model):
    titulo= models.CharField(max_length=20, default='')
    tags = models.ManyToManyField('Tag', blank=True)

class Tag(models.Model):
    nombre = models.CharField(max_length=20, default='')
    noticias = models.ManyToManyField('Noticia', through=Noticia.tags.through, blank=True)

class Test1(models.Model):
    nombre= models.CharField(max_length=20, default='')
    tests2 = models.ManyToManyField('Test2', blank=True)

class Test2(models.Model):
    nombre = models.CharField(max_length=20, default='')
    tests1 = models.ManyToManyField('Test1', through=Test1.tests2.through, blank=True)