from django.db import models

class WeekDayAvailability(models.IntegerChoices):
    AVAILABLE = 0, 'Available'
    NOT_AVAILABLE = 1, 'Not available'

class Calendar(models.Model):
    service_id = models.CharField(max_length=255, primary_key=True)
    monday = models.IntegerField(blank=False, null=False, choices=WeekDayAvailability.choices)
    tuesday = models.IntegerField(blank=False, null=False, choices=WeekDayAvailability.choices)
    wednesday = models.IntegerField(blank=False, null=False, choices=WeekDayAvailability.choices)
    thursday = models.IntegerField(blank=False, null=False, choices=WeekDayAvailability.choices)
    friday = models.IntegerField(blank=False, null=False, choices=WeekDayAvailability.choices)
    saturday = models.IntegerField(blank=False, null=False, choices=WeekDayAvailability.choices)
    sunday = models.IntegerField(blank=False, null=False, choices=WeekDayAvailability.choices)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)