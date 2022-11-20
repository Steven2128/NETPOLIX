# Django
from django.urls import path, include
# DRF
from rest_framework.routers import DefaultRouter
# Views
from .views import *

router = DefaultRouter()
router.register('film', FilmModelViewSet, basename='film')
router.register('category', CategoryModelViewSet, basename='category')
router.register('language', LanguageModelViewSet, basename='language')
router.register('actor', ActorModelViewSet, basename='actor')
router.register('classification', ClassificationModelViewSet, basename='classification')
router.register('serie', SerieModelViewSet, basename='serie')
router.register('collection', CollectionModelViewSet, basename='collection')


urlpatterns = [
    path('api/', include(router.urls)),
    path('', FilmsTemplateView.as_view(), name='film-list'),
    path('videos/<slug:slug>/', FilmsDetailView.as_view(), name='film-detail'),
    path('idioma-original/', FilmsOriginLanguageView.as_view(), name='film-original-languages'),
    path('idioma-subtitulado/', FilmsSubtitledLanguageView.as_view(), name='film-subtitled-languages'),
    path('idioma-doblado/', FilmsDubbedLanguageView.as_view(), name='film-dubbed-languages'),
    path('series/', SeriesTemplateView.as_view(), name='serie-list'),
    path('chaper/list/<slug:slug>/', ChaptersListView.as_view(), name='chapter-list'),
]