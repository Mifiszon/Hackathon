from django.db import models

class LocationType(models.IntegerChoices):
    STOP = 0, 'Stop'
    STATION = 1, 'Station'
    ENTRANCE_EXIT = 2, 'Entrance/Exit'
    GENERIC_NODE = 3, 'Generic node'
    BOARDING_AREA = 4, 'Boarding area'


class Stops(models.Model):
    stop_id = models.CharField(max_length=255, primary_key=True)
    stop_code = models.CharField(max_length=255, blank=True, null=True)
    stop_name = models.CharField(max_length=255)
    stop_desc = models.CharField(max_length=255, blank=True, null=True)
    stop_lat = models.FloatField()
    stop_lon = models.FloatField()
    stop_url = models.TextField(blank=True, null=True)
    location_type = models.IntegerField(blank=True, null=True, choices=LocationType.choices)
    parent_station = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)