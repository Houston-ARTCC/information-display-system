from django.db import models


class Facility(models.Model):
    icao = models.CharField(max_length=4)
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'[{self.icao}] {self.name}'
