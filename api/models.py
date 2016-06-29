from django.db import models


class Color(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=40)
    descripcion = models.CharField(blank=True, unique=True, max_length=140)
    hexadecimal = models.CharField(max_length=7, unique=True)
    red = models.PositiveSmallIntegerField()
    green = models.PositiveSmallIntegerField()
    blue = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class ColorPalette(models.Model):
	name= models.CharField(unique=True,max_length=140)
	descripcion = models.CharField(max_length=500)
	colors = models.ManytoManyField(Color)

	def __str__(self):
		return self.name