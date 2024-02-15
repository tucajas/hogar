from django.db import models
from impuesto.models import Impuesto

# Create your models here.

class Cuenta (models.Model):
    impuesto            = models.ForeignKey(Impuesto,on_delete=models.CASCADE, related_name='impuesto')
    fechaVencimiento    = models.DateField()
    fechaPago           = models.DateField()
    importePagar        = models.FloatField()
    importePagado       = models.FloatField()
    cantidadCuotas      = models.IntegerField()
    

    def __str__(self) :
        return str(self.impuesto)