# Django
from django.urls import path, include
# DRF
from rest_framework.routers import DefaultRouter
# Views
from .views import *

router = DefaultRouter()
router.register('', UserModelViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]