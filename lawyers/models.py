from django.db import models
from django_google_maps import fields as map_fields
from places.fields import PlacesField

# geoposition
from geoposition.fields import GeopositionField

class Poi(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()


    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Points of interest"

class Area(models.Model):
    location = PlacesField()


class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=200)


    class Meta:
        verbose_name_plural = "Rentals"

    def __str__(self):
        return self.address

        

class Post(models.Model):
    heading = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return f'Post {self.heading}'

class Like(models.Model):
    post = models.ForeignKey(Post,related_name='post_likes')

class Leaf(models.Model):
    name = models.CharField(max_length=120)
    geom = models.CharField(max_length=255)
    