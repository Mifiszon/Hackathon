from django.db import models
from .Trips import Trips
from .Stops import Stops

class PickupType(models.IntegerChoices):
    REGULARLY_SCHEDULED = 0, 'Regularly scheduled'
    NO_PICKUP_AVAILABLE = 1, 'No pickup available'
    MUST_PHONE_AGENCY = 2, 'Must phone agency'
    MUST_COORDINATE_WITH_DRIVER = 3, 'Must coordinate with driver'
    
class DropOffType(models.IntegerChoices):
    REGULARLY_SCHEDULED = 0, 'Regularly scheduled'
    NO_DROP_OFF_AVAILABLE = 1, 'No drop off available'
    MUST_PHONE_AGENCY = 2, 'Must phone agency'
    MUST_COORDINATE_WITH_DRIVER = 3, 'Must coordinate with driver'

class StopTimes(models.Model):
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stops, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    stop_sequence = models.IntegerField()
    stop_headsign = models.CharField(max_length=255, blank=True, null=True)
    pickup_type = models.IntegerField(blank=True, null=True, choices=PickupType.choices)
    drop_off_type = models.IntegerField(blank=True, null=True, choices=DropOffType.choices)
    shape_dist_traveled = models.FloatField(blank=True, null=True)