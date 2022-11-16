# Django
from django.db import models
# Models users
from users.models import User
# Models films
from films.models import Film


class Transaction(models.Model):
    """Model Transaction"""
    TYPE_TRANSACTIONS = [
        ('C', 'Comprar'),
        ('A', 'Alquilar')
    ]
    date_transaction = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de transacción')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cliente quien hizo la transacción')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Película')
    type_transaction = models.CharField(max_length=1, choices=TYPE_TRANSACTIONS, null=False, blank=False, verbose_name='Tipo de transacción')
    start_time_rent = models.DateField(auto_now=False, auto_now_add=True, null=True, blank=True, verbose_name='Fecha inicio del alquiler')
    end_time_rent = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='Fecha fin del alquiler')

    def __str__(self):
        return "{} {}".format(self.date_transaction, self.client.get_full_name())

    class Meta:
        verbose_name = 'Transacción'
        verbose_name_plural = 'Transacciones'