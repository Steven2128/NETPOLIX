# Django
from django.urls import path, include
# Views
from .views import *



urlpatterns = [
    path('', PQRCreateView.as_view(), name='pqr_index'),
]