from django.db import models

# Create your models here.

class password(models.Model):
	key = models.CharField(max_length = 15)
	state = models.IntegerField(default=0)

class Registration(models.Model):
	teamname = models.CharField(max_length=100)
	key = models.OneToOneField(password, primary_key=True)
	name1 = models.CharField(max_length=100)
	email1 = models.CharField(max_length=100)
	git1 = models.CharField(max_length=50)
	ph1 = models.CharField(max_length=15)
	name2 = models.CharField(max_length=100)
	email2 = models.CharField(max_length=100)
	git2 = models.CharField(max_length=50)
	ph2 = models.CharField(max_length=15)
	name3 = models.CharField(max_length=100)
	email3 = models.CharField(max_length=100)
	git3 = models.CharField(max_length=50)
	ph3 = models.CharField(max_length=15)
	name4 = models.CharField(max_length=100)
	email4 = models.CharField(max_length=100)
	git4 = models.CharField(max_length=50)
	ph4 = models.CharField(max_length=15)

	def __unicode__(self):
		return self.teamname
