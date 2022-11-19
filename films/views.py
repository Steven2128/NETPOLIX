# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView
# DRF
from rest_framework import viewsets, generics
# Models
from .models import *
# Models transactions
from transactions.models import *
# Serializers
from .serializers import *
# Datetime
from datetime import datetime


class FilmModelViewSet(viewsets.ModelViewSet):
    """Film Model View Set"""
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def perform_create(self, serializer):
        serializer.save()


class CategoryModelViewSet(viewsets.ModelViewSet):
    """Category Model View Set"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LanguageModelViewSet(viewsets.ModelViewSet):
    """Language Model View Set"""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ActorModelViewSet(viewsets.ModelViewSet):
    """Language Model View Set"""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ClassificationModelViewSet(viewsets.ModelViewSet):
    """Clasification Model View Set"""
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class SerieModelViewSet(viewsets.ModelViewSet):
    """Serie Model view Set"""
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class CollectionModelViewSet(viewsets.ModelViewSet):
    """Colecction Model View Set"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class FilmsTemplateView(LoginRequiredMixin, TemplateView):
    """Films Template View"""
    template_name = 'films/index.html'

    def get_context_data(self, **kwargs):
        context = super(FilmsTemplateView, self).get_context_data(**kwargs)
        # here's the difference:
        context['films'] = Film.objects.all()
        return context


class FilmsDetailView(LoginRequiredMixin, DetailView):
    """Film Detail View"""
    model = Film
    template_name = 'films/anime-details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_object(self, **kwargs):
        return Film.objects.get(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(FilmsDetailView, self).get_context_data(**kwargs)
        # here's the difference:
        context['films'] = Film.objects.filter(slug=self.slug_url_kwarg)
        context['transaction_buy'] = Transaction.objects.filter(film=self.get_object(), client=self.request.user, type_transaction='C').count()
        transaction_rent = Transaction.objects.filter(film=self.get_object(), client=self.request.user, type_transaction='A').last()
        try:
            if datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d').date() >= transaction_rent.end_time_rent:
                context['transaction_rent_able'] = True
            else:
                context['transaction_rent_able'] = False
                context['transaction_rent'] = transaction_rent
        except Exception as Ex:
            print(Ex)
        return context
