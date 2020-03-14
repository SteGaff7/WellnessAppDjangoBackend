from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class CheckAuth(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)

        content = {'message': 'You are authorized'}

        return Response(content, status=200)