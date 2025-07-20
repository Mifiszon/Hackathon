from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from kosciuszkon.models import Routes, Trips
from kosciuszkon.serializers import RoutesSerializer, TripsSerializer

class TripsApiView(APIView):

    @swagger_auto_schema(
        responses={200: "Ok", 404: "Not Found"},
    )
    def get(self, request, routeId = None):
        if routeId:
            try:
                route = Routes.objects.get(route_id=routeId)
                trips = Trips.objects.filter(route=route)
                serialized = TripsSerializer(trips, many=True)
                
                return Response(serialized.data, status=status.HTTP_200_OK)
            except:
                return Response('No object with given id',status=status.HTTP_204_NO_CONTENT)
        else:
            routes = Routes.objects.all()
            return Response(routes.values(), status=status.HTTP_200_OK)