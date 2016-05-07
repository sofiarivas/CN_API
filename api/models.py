from django.db import models


class Color(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=40)
    hexadecimal = models.CharField(max_length=7, unique=True)
    red = models.PositiveSmallIntegerField()
    green = models.PositiveSmallIntegerField()
    blue = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name