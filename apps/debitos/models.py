from django.db import models
from django.utils.datetime_safe import date
from .choices import *


class Debitos(models.Model):
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    produto = models.CharField(max_length=200)
    observacao = models.TextField(max_length=200)
    categoria = models.CharField(choices=CATEGORIA_DEBITOS_CHOICE, max_length=30)
    tipo = models.CharField(choices=TIPO_CHOICE, max_length=20)
    status = models.CharField(default='-', choices=STATUS_CHOICE, max_length=10)
    parcelas = models.CharField(default='-', choices=PARCELAMENTO_CHOICE, max_length=10)
    vencimento = models.DateField(default=date.today)
    credor = models.CharField(max_length=200)
    valor_total = models.DecimalField(max_digits=20, decimal_places=2)
    hrs_trab_pagar = models.DecimalField(max_digits=20, decimal_places=2)

    def save(self, *args, **kwargs):
        if not float(self.parcelas) == 0:
            self.valor_total = float(self.valor) * float(self.parcelas)
        else:
            self.valor_total = float(self.valor)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.valor) + ' ' + self.produto + ' ' + self.observacao + ' ' + self.categoria_debitos