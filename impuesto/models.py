from django.db import models

# Create your models here.

class Impuesto (models.Model):
    nombre      = models.CharField(max_length=20)

    def __str__(self) :
        return str(self.nombre)