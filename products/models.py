from django.db import models

# Create your models here.

class Product(models.Model):
	description = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.IntegerField()
	image = models.ImageField(upload_to='images')

	def __str__(self):
		return self.description
