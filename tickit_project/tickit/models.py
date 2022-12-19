from django.db import models
from django.db.models import Model

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=100)
    address= models.TextField(max_length=200)
    description= models.TextField(max_length=300, null=True)
    onsite_parking= models.BooleanField(null=True)
    capacity= models.IntegerField(null=True, blank=True)
    photo_url= models.TextField(null=True, max_length=500)

    def __str__(self):
        return self.name

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name= 'events')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description= models.TextField(max_length=500)
    ASL_interpreter= models.BooleanField(null=True)
    date= models.CharField(null=True, max_length=100)
    alcohol_served= models.BooleanField(null=True)
    photo_url= models.TextField(null=True, max_length=500, blank=True)

    def __str__(self):
        return self.name
