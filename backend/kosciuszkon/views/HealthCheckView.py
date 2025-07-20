from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class HealthCheckView(APIView):

    @swagger_auto_schema(
        responses={200: "Ok", 404: "Not Found"},
    )
    def get(self, request):
        return Response({'status': 'ok'})