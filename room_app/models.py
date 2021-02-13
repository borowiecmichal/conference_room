from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=64, unique=True)
    capacity = models.IntegerField()
    projector_availability = models.BooleanField()

