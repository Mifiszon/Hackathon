from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from kosciuszkon.models import StopTimes, Trips, Routes
from kosciuszkon.serializers import RoutesSerializer

class ResourceApiView(APIView):
    
    @swagger_auto_schema(
        responses={200: 'OK'},
    )
    def get(self, request, id = None):
        
        if id:
            try:
                route = Routes.objects.get(route_id=id)
                serialized = RoutesSerializer(route)
                
                # print(route)
                return Response(serialized.data, status=status.HTTP_200_OK)
            except:
                return Response('No object with given id',status=status.HTTP_204_NO_CONTENT)
        else:
            routes = Routes.objects.all()
            return Response(routes.values(), status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    