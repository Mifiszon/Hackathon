from rest_framework import serializers
from kosciuszkon.models import Stops

class StopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stops
        fields = '__all__'