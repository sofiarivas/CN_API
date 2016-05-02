from django.db import models


class Colors(models.Model):
    name = models.CharField(blank=True, unique=True, max_length= 40)
    hex = models.CharField(max_length=7, unique=True)
