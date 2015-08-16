from django.db import models

# Create your models here.

class password(models.Model):
	key = models.CharField(max_length = 15)
	state = models.IntegerField(default=0)
