from rest_framework import serializers
from kosciuszkon.models import Shapes

class ShapesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shapes
        fields = '__all__'

        