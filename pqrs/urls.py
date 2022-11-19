# Django
from django.urls import path, include
# DRF
from rest_framework.routers import DefaultRouter
# Views
from .views import *

router = DefaultRouter()
router.register('', PQRModelViewSet, basename='pqr')

urlpatterns = [
    path('', include(router.urls)),
    # path('create/', PQRCreateView.as_view(), name='pqr_index'),
]