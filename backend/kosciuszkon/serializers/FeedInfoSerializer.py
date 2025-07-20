from rest_framework import serializers
from kosciuszkon.models import FeedInfo

class FeedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedInfo
        fields = '__all__'