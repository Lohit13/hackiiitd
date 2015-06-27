from django.db import models

# Create your models here.

class password(models.Model):
	uid = models.AutoField(primary_key = True)
	key = models.CharField(max_length = 15)
