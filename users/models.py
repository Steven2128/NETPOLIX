# Django
import secrets

from django.contrib.auth.models import User, AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class User(AbstractUser):
    """Model User"""
    is_client = models.BooleanField(default=False, verbose_name='¿Es cliente?')
    is_employee = models.BooleanField(default=False, verbose_name='¿Es empleado?')
    is_administrator = models.BooleanField(default=False, verbose_name='¿Es administrador?')
    identification = models.CharField(max_length=20, blank=False, null=False, verbose_name='Identificación')
    code = models.CharField(max_length=50, blank=False, null=False, unique=True, verbose_name='Codigo promocional')
    current_points = models.PositiveIntegerField(blank=False, null=False, default=0, verbose_name='Puntos acumulados')
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'bpm', 'jpeg', 'jpe'])])

    def __str__(self):
        return "{} - {}".format(self.get_full_name(), self.email)

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'


# class Client(models.Model):
#     """Model Client"""
#     user = models.OneToOneField("users.User", on_delete=models.CASCADE)
#     identification = models.CharField(max_length=20, blank=False, null=False, verbose_name='Identificación')
#     current_points = models.PositiveIntegerField(blank=False, null=False, default=0, verbose_name='Puntos acumulados')
#
#     def __str__(self):
#         return "{} - {} - Puntos actuales: ".format(self.user.get_full_name(), self.identification, self.current_points)
#
#     class Meta:
#         verbose_name = 'Cliente'
#         verbose_name_plural = 'Clientes'
