from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Equipment(models.Model):
    type = models.CharField(max_length=35)
    brand = models.CharField(max_length=35)
    model = models.CharField(max_length=35)
    quantity = models.IntegerField()
    rented = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)