from django.db import models

class Agency(models.Model):
    agency_id = models.CharField(max_length=255, primary_key=True)
    agency_name = models.CharField(max_length=255)
    agency_url = models.URLField()
    agency_timezone = models.CharField(max_length=255)
    agency_lang = models.CharField(max_length=10, blank=True, null=True)
    agency_phone = models.CharField(max_length=20, blank=True, null=True)
    agency_fare_url = models.URLField(blank=True, null=True)
    agency_email = models.TextField(blank=True, null=True)