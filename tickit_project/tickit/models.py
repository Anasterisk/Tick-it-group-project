from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=100)
    address= models.TextField(max_length=500)
    onsite_parking: models.BooleanField
    capacity: models.IntegerField
    photo_url: models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name= 'events')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description= models.TextField(max_length=500)
    onsite_parking: models.BooleanField
    date: models.CharField(max_length=100)
    alcohol_served: models.BooleanField
    photo_url: models.CharField(max_length=500)

    def __str__(self):
        return self.name
