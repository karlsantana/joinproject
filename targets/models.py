from django.db import models

class Alvo(models.Model):
    nome = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    data_expiracao = models.DateField()

    def __str__(self):
        return self.nome
