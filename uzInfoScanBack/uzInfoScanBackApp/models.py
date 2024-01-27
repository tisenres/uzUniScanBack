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
    Sana = models.DateField()
    Raqam = models.IntegerField()
    Muddati = models.DateField()
