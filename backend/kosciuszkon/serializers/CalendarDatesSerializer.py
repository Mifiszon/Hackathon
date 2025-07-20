from rest_framework import serializers
from kosciuszkon.models import CalendarDates
from .CalendarSerializer import CalendarSerializer
class CalendarDatesSerializer(serializers.ModelSerializer):
    service_id = CalendarSerializer()
    class Meta:
        model = CalendarDates
        fields = '__all__'