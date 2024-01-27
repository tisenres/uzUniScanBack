from datetime import datetime

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class LombardModel(models.Model):
    STIR = models.CharField(max_length=20)
    Nomi = models.CharField(max_length=255)
    Manzil = models.TextField()
    Sana = models.CharField(max_length=10)
    Raqam = models.CharField(max_length=10)
    Muddati = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.Nomi} - {self.Raqam}"