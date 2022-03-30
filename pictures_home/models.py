from django.db import models

# Create your models here.

class Artist(models.Model):
	name = models.CharField(max_length = 200 )
	date_of_born = models.CharField(max_length = 200)
	date_of_death = models.CharField(max_length = 200)
	photo = models.ImageField(upload_to = "photo_artist/")
	history = models.TextField(blank=True)

	
	def __str__(self):
		return self.name


class Picture(models.Model):

	artist = models.ForeignKey('Artist', on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)
	style = models.CharField(max_length = 200)
	discribe = models.TextField(blank=True)
	picture = models.ImageField(upload_to = "pictures/")
	date_of_create = models.CharField(max_length = 200)

	def __str__(self):
		return self.name