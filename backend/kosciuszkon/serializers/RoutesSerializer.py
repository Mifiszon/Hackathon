from rest_framework import serializers
from kosciuszkon.models import Routes

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'