from django.db import models

# Create your models here.

class About(models.Model):

	short_description = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='about/')

	class Meta:
		verbose_name = 'About Me'
		verbose_name_plural = 'About Me'

	def __str__(self):
		return "About Me"



class Service(models.Model):
	
	name = models.CharField(max_length=100, verbose_name='Service Name')
	description = models.TextField()

	def __str__(self):
		return self.name




class RecentWork(models.Model):

	title = models.CharField(max_length=100, verbose_name='Work Title')
	image = models.ImageField(upload_to='work/')

	def __str__(self):
		return self.title



class Client(models.Model):

	name = models.CharField(max_length=100, verbose_name='Client Name')
	description = models.TextField(verbose_name='Client Comment')
	image = models.ImageField(upload_to='client')

	def __str__(self):
		return self.name