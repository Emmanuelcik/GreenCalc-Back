from rest_framework.response import Response
from .serializer import EnterprizeSerlizer
from rest_framework import status
from rest_framework.views import APIView


class EnterprizeAPI(APIView):
    def post(self, request):
        serializer = EnterprizeSerlizer(data = request.data)
        if(serializer.is_valid()):
            enterprize = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
