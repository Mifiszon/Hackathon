from django.db import models
from .Agency import Agency

class TransportTypes(models.IntegerChoices):
    TRAM_STREETCAR_LIGHT_RAIL = 0, 'Tram, Streetcar, Light rail'
    SUBWAY_METRO = 1, 'Subway, Metro'
    RAIL = 2, 'Rail'
    BUS = 3, 'Bus'
    FERRY = 4, 'Ferry'
    CABLE_TRAM = 5, 'Cable tram'
    AERIAL_LIFT = 6, 'Aerial lift'
    FUNICULAR = 7, 'Funicular'
    TROLLEYBUS = 11, 'Trolleybus'
    MONORAIL = 12, 'Monorail'

class Routes(models.Model):
    route_id = models.CharField(max_length=255, primary_key=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=True, null=True)
    route_short_name = models.CharField(max_length=255)
    route_long_name = models.CharField(max_length=255)
    route_desc = models.CharField(max_length=255, blank=True, null=True)
    route_type = models.IntegerField(choices=TransportTypes.choices)
    route_url = models.TextField(blank=True, null=True)
    route_color = models.CharField(max_length=6, blank=True, null=True)
    route_text_color = models.CharField(max_length=6, blank=True, null=True)