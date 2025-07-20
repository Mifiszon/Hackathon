from rest_framework import serializers
from kosciuszkon.models import Trips
from .RoutesSerializer import RoutesSerializer
from .CalendarSerializer import CalendarSerializer
from .ShapesSerializer import ShapesSerializer

class TripsSerializer(serializers.ModelSerializer):
    route = RoutesSerializer()
    service = CalendarSerializer()
    shape_id = ShapesSerializer()
    class Meta:
        model = Trips
        fields = '__all__'