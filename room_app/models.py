from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=64, unique=True)
    capacity = models.IntegerField()
    projector_availability = models.BooleanField()

class Reservation(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField(default='')

    class Meta:
        unique_together = ('date', 'room',)
        ordering = ['date']