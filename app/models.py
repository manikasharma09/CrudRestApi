from django.db import models

class Profile(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	description=models.CharField(max_length=200)


	def __str__(self):
		return self.name
