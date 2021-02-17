from django.db import models
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=64, unique=True)
    capacity = models.IntegerField()
    projector_availability = models.BooleanField()

    def status(self):
        today = datetime.today()
        try:
            Reservation.objects.get(date=today, room=self)
            return "✗"
        except:
            return "✓"


class Reservation(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField(default='')

    class Meta:
        unique_together = ('date', 'room',)
        ordering = ['date']
