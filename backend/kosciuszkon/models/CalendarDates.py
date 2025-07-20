from django.db import models
from .Calendar import Calendar

class ExceptionType(models.IntegerChoices):
    SERVICE_ADDED = 1, 'Service added'
    SERVICE_REMOVED = 2, 'Service removed'

class CalendarDates(models.Model):
    service_id = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    date = models.DateField()
    exception_type = models.IntegerField(choices=ExceptionType.choices)