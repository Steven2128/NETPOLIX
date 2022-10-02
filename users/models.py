# Django
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    """Model Client"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identification = models.CharField(max_length=20, blank=False, null=False, verbose_name='Identificación')
    current_points = models.PositiveIntegerField(blank=False, null=False, default=0, verbose_name='Puntos acumulados')

    def __str__(self):
        return "{} - {} - Puntos actuales: ".format(self.user.get_full_name(), self.identification, self.current_points)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
