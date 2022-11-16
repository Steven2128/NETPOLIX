# Django
from django.urls import path, include
# Views
from .views import *


urlpatterns = [
    path('buy/<str:title>/', buy_film, name='buy-film'),
    path('rent/<str:title>/', rent_film, name='rent-film'),
]