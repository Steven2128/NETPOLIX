# Django
from django.shortcuts import render, redirect
# Models
from .models import *
# Models films
from films.models import *
# Datetime
from datetime import datetime, timedelta


def buy_film(request, title):
    """Buy film"""
    film = Film.objects.get(slug=title)
    transactions = Transaction.objects.filter(film=film, client=request.user, type_transaction='C').count()
    if transactions == 0:
        Transaction.objects.create(client=request.user, film=film, type_transaction='C')
    return redirect('film-detail', title)


def rent_film(request, title):
    """Rent film"""
    film = Film.objects.get(slug=title)
    transaction = Transaction.objects.filter(film=film, client=request.user, type_transaction='C').count()
    if transaction == 0:
        Transaction.objects.create(client=request.user, film=film, type_transaction='A', end_time_rent=datetime.today() + timedelta(days=1))
    return redirect('film-detail', title)