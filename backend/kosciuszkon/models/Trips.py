from django.db import models
from .Routes import Routes
from .Calendar import Calendar
from .Shapes import Shapes

class DirectionType(models.IntegerChoices):
    OUTBOUND = 0, 'Outbound'
    INBOUND = 1, 'Inbound'

class WheelchairAccessibleType(models.IntegerChoices):
    NO_INFORMATION = 0, 'No information'
    ACCESSIBLE = 1, 'Accessible'
    NOT_ACCESSIBLE = 2, 'Not accessible'

class Trips(models.Model):
    trip_id = models.CharField(max_length=255, primary_key=True)
    route = models.ForeignKey(Routes, on_delete=models.CASCADE)
    service = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    trip_headsign = models.CharField(max_length=255, blank=True, null=True)
    trip_short_name = models.CharField(max_length=255, blank=True, null=True)
    direction_id = models.IntegerField(blank=True, null=True, choices=DirectionType.choices)
    block_id = models.CharField(max_length=255, blank=True, null=True)
    shape_id = models.ForeignKey(Shapes, on_delete=models.CASCADE, blank=True, null=True)
    wheelchair_accessible = models.IntegerField(blank=True, null=True, choices=WheelchairAccessibleType.choices)