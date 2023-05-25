# Create your models here.
from django.db import models

class coin_day(models.Model):
    id = models.CharField('id', max_length=20, primary_key=True)
    date_part = models.CharField('date_part', max_length=10)
    name = models.CharField('name', max_length=10)
    value = models.FloatField()

    def __str__(self):
        return str(self.date_part) + ' | ' + str(self.name) + ' | ' + str(self.value)
