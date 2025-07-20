from django.db import models

class Shapes(models.Model):
    shape_id = models.IntegerField(blank=False, null=False)
    shape_pt_lat = models.FloatField(blank=False, null=False)
    shape_pt_lon = models.FloatField(blank=False, null=False)
    shape_pt_sequence = models.PositiveIntegerField(blank=False, null=False)
    shape_dist_traveled = models.FloatField(blank=False, null=True)