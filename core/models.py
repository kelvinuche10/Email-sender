from django.db import models

# Create your models here.

class Detail(models.Model):
	f_name = models.CharField(max_length=200, blank=True)
	l_name = models.CharField(max_length=200, blank=True)
	email = models.EmailField()

	def __str__(self):
		return self.f_name