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
router.register('classification', ClassificationModelViewSet, basename='classification')
router.register('serie', SerieModelViewSet, basename='serie')
router.register('collection', CollectionModelViewSet, basename='collection')


urlpatterns = [
    path('', include(router.urls)),
]