from rest_framework import serializers
from kosciuszkon.models import StopTimes
from .StopsSerializer import StopsSerializer
from .TripsSerializer import TripsSerializer
class StopTimesSerializer(serializers.ModelSerializer):
    trip = TripsSerializer()
    stop = StopsSerializer()
    class Meta:
        model = StopTimes
        fields = '__all__'