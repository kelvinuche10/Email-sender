from django.db import models

# Create your models here.

class Detail(models.Model):
	email = models.EmailField()

	# def __str__(self):
	# 	return self.f_name