# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView
# DRF
from rest_framework import viewsets
# Models
from .models import *
# Serializers
from .serializers import *


class FilmModelViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def perform_create(self, serializer):
        serializer.save()


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LanguageModelViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ClassificationModelViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class SerieModelViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class CollectionModelViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class FilmsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'films/index.html'

    def get_context_data(self, **kwargs):
        context = super(FilmsTemplateView, self).get_context_data(**kwargs)
        # here's the difference:
        context['films'] = Film.objects.all()
        return context


class FilmsDetailView(LoginRequiredMixin, DetailView):
    model = Film
    template_name = 'films/anime-details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_object(self, **kwargs):
        return Film.objects.get(slug=self.kwargs['slug'])
