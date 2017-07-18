from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    """
        An object to represent a single event. This is created by the Event Manager.
    """
    name = models.CharField(max_length=120)
    time = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Group(models.Model):
    """
        This represents a group of people. It's just an ID for now, but we
        will store the date of creation eventually.
    """
    def __str__(self):
        return str(self.pk)

class Booking(models.Model):
    """
        This is an individual booking for a specific event, by a specific user,
        who in turn is attached to a specific group.
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    dietary_requirements = models.TextField(blank=True)
    wine_choice = models.CharField(max_length=50, blank=True)
