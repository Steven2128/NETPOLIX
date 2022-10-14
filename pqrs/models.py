# Django
from django.db import models
# Models users
from users.models import User


class PQR(models.Model):
    """Model PQR"""
    REQUEST_TYPE_CHOICES = [
        ('', 'Seleccione el tipo de solicitud'),
        ('P', 'Pregunta'),
        ('Q', 'Queja'),
        ('R', 'Reclamo')
    ]
    request_type = models.CharField(max_length=1, choices=REQUEST_TYPE_CHOICES, blank=False, null=False, verbose_name='Tipo de solicitud')
    request_detail = models.TextField(blank=False, null=False, verbose_name='Detalle de la solicitud')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cliente que radica el PQR')

    def __str__(self):
        return "{} - {}".format(self.get_request_type_display(), self.client.get_full_name())

    class Meta:
        verbose_name = 'PQR'
        verbose_name_plural = 'PQRs'