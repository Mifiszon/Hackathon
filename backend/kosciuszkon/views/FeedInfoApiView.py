from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from kosciuszkon.models import FeedInfo
from kosciuszkon.serializers import FeedInfoSerializer

class FeedInfoApiView(APIView):
    
    @swagger_auto_schema(
        responses={200: "Ok", 404: "Not Found"},
    )
    def get(self, request, id = None):
        if id:
            calendar = FeedInfo.objects.get(service_id=id)
            serialized = FeedInfoSerializer(calendar)
            return Response(serialized.data)
        else:
            calendar = FeedInfo.objects.all()
            return Response(calendar.values())
        
        return Response(status=status.HTTP_204_NO_CONTENT)