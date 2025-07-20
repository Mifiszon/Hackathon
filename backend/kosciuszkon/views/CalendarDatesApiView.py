from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from kosciuszkon.models import CalendarDates
from kosciuszkon.serializers import CalendarDatesSerializer

class CalendarDatesApiView(APIView):
    
    @swagger_auto_schema(
        responses={200: "Ok", 404: "Not Found"},
    )
    def get(self, request, id = None):
        if id:
            calendar = CalendarDates.objects.get(service_id=id)
            serialized = CalendarDatesSerializer(calendar)
            return Response(serialized.data)
        else:
            calendar = CalendarDates.objects.all()
            return Response(calendar.values())
        
        return Response(status=status.HTTP_204_NO_CONTENT)