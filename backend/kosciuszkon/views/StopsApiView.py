import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from kosciuszkon.models import Stops, StopTimes, Trips
from kosciuszkon.serializers import StopsSerializer, StopTimesSerializer

logger = logging.getLogger(__name__)

class StopsApiView(APIView):

    @swagger_auto_schema(
        responses={200: 'OK'},
    )
    def get(self, request, id=None):
        if id:
            try:
                trip = Trips.objects.filter(trip_id=id)
                if not trip.exists():
                    logger.error(f"No Stops found with given id: {id}")
                    return Response({'error': f'No trips found with given id: {id}'}, status=status.HTTP_404_NOT_FOUND)
                
                stop_time = StopTimes.objects.filter(trip_id=trip[0].trip_id)
                if not stop_time.exists():
                    logger.error(f"No StopTimes found for stop_id: {trip[0].trip_id}")
                    return Response({'error': f'No StopTimes found for stop_id: {trip[0].trip_id}'}, status=status.HTTP_404_NOT_FOUND)
                
                stop_time_serializer = StopTimesSerializer(stop_time, many=True)
                # Ensure all values are JSON compliant
                stop_time_data = stop_time_serializer.data
                for entry in stop_time_data:
                    for key, value in entry.items():
                        if value is None or isinstance(value, float) and (value != value or value in [float('inf'), float('-inf')]):
                            entry[key] = "null"  # Replace invalid values with string "null"

                return Response(stop_time_data, status=status.HTTP_200_OK)
            except Exception as e:
                logger.error(f"Error occurred: {str(e)}")
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                routes = Stops.objects.all()
                routes_serializer = StopsSerializer(routes, many=True)
                return Response(routes_serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                logger.error(f"Error occurred while fetching all routes: {str(e)}")
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
