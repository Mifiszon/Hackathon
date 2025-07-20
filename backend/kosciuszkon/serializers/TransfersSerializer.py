from rest_framework import serializers
from kosciuszkon.models import Transfers
from .StopsSerializer import StopsSerializer
class TransfersSerializer(serializers.ModelSerializer):
    from_stop = StopsSerializer()
    to_stop = StopsSerializer()
    class Meta:
        model = Transfers
        fields = '__all__'