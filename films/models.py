# Django
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """Model Category"""
    description = models.CharField(max_length=50, blank=False, null=False, verbose_name='Descripción')

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.description


class Classification(models.Model):
    """Model classification"""
    description = models.CharField(max_length=50, blank=False, null=False, verbose_name='Descripción')
    type = models.CharField(max_length=50, blank=False, null=False, verbose_name='Tipo de clasificación')

    class Meta:
        verbose_name = "Clasificación"
        verbose_name_plural = 'Clasificaciones'
        ordering = ['description']

    def __str__(self):
        return self.description


class Language(models.Model):
    """Model Language"""
    language = models.CharField(max_length=30, blank=False, null=False, verbose_name='Idioma')
    type = models.CharField(max_length=50, blank=False, null=False, verbose_name='Tipo de idioma')

    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = 'Idiomas'

    def __str__(self):
        return "{} {}".format(self.language, self.type)


class Actor(models.Model):
    """Model Actor"""
    full_name = models.CharField(max_length=70, blank=False, null=False, verbose_name='Nombre completo')

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = 'Actores'

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.full_name = self.full_name.title()
        super(Actor, self).save(*args, **kwargs)


class Film(models.Model):
    """Model Film"""
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name='Titulo original')
    year = models.PositiveIntegerField(blank=False, null=False, verbose_name='Año de publicación')
    duration = models.PositiveIntegerField(blank=False, null=False, verbose_name='Duración en minutos')
    ISAN = models.CharField(max_length=96, blank=False, null=False, verbose_name='ISAN')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    language = models.ManyToManyField(Language, related_name='film_language', verbose_name='Idiomas')
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, verbose_name='Clasificación')
    image_thumbnail = models.ImageField(upload_to='films/img/', null=True, blank=True, verbose_name="Foto Miniatura")
    review_short = models.TextField(blank=True, null=True, verbose_name='Argumento corto')
    # film_url = models.URLField(max_length=150, null=False, blank=False, verbose_name='Url de la película')
    movie = models.FileField(upload_to='films/', null=False, blank=False, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], default='films/default.mp4', verbose_name='Película')
    actors = models.ManyToManyField(Actor, related_name="film_actor", verbose_name="Actores")
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = 'películas'
        ordering = ['title']

    def __str__(self):
        return "{} {}".format(self.title, self.year)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Film, self).save(*args, **kwargs)


class Serie(models.Model):
    """Model Serie"""
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name='Titulo original')
    season = models.PositiveIntegerField(blank=False, null=False, default=0, verbose_name='Temporada')
    fimls = models.ManyToManyField(Film, related_name='fimls_serie', verbose_name='Peliculas')
    image_thumbnail = models.ImageField(upload_to='series/img/', null=True, blank=True, verbose_name="Foto Miniatura")
    slug = models.SlugField(unique=True, blank=True, null=True)
    main_character = models.CharField(max_length=150, blank=True, null=True, verbose_name='Prsonaje principal')

    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = 'Series'
        ordering = ['title']

    def __str__(self):
        return "{} - Temporada: {}".format(self.title, self.season)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Serie, self).save(*args, **kwargs)


class Collection(models.Model):
    """Model Collection"""
    ISAN = models.CharField(max_length=96, blank=False, null=False, verbose_name='ISAN')
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name='Titulo original')
    volume = models.PositiveIntegerField(blank=False, null=False, default=0, verbose_name='Volumen')
    fimls = models.ManyToManyField(Film, related_name='fimls_collection', verbose_name='Peliculas')

    class Meta:
        verbose_name = "Colección"
        verbose_name_plural = 'Colecciones'
        ordering = ['title']

    def __str__(self):
        return "{} - Volumen: {}".format(self.title, self.volume)
