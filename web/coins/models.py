from django.db import models


# Create your models here.

class coinlayer_historical(models.Model):
    date_part = models.CharField('date_part', max_length=10, primary_key=True)
    name = models.CharField('name', max_length=10, primary_key=True)
    value = models.FloatField()

    def __str__(self):
        return str(self.date_part) + "|" + str(self.name) + "|" + str(self.value)
