# Django
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render, redirect
# Models
from rest_framework import generics

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
        user = User.objects.filter(pk=request.user.pk).first()
        user.amount_transactions += 1
        user.save()
        messages.success(request, "¡Compra realizada con exito!")
    return redirect('film-detail', title)


def rent_film(request, title):
    """Rent film"""
    film = Film.objects.get(slug=title)
    transaction = Transaction.objects.filter(film=film, client=request.user, type_transaction='C').count()
    if transaction == 0:
        transaction = Transaction.objects.create(client=request.user, film=film, type_transaction='A', end_time_rent=datetime.today() + timedelta(days=1))
        user = User.objects.filter(pk=request.user.pk).first()
        user.amount_transactions += 1
        user.save()
        messages.success(request, "¡Alquiler realizado con exito! \n Puedes visualizar esta pelicula hasta: " + transaction.end_time_rent.strftime('%Y/%m/%d'))

    return redirect('film-detail', title)


