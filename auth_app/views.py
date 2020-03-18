from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.serializers import UserSerializer

from rest_framework.authtoken.models import Token

class CheckAuth(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)

        content = {'message': 'You are authorized'}

        return Response(content, status=200)


class Register(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        print(data)

        # Serialize data into user

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            instance = serializer.save()
            # Try obtain auth token here and return it after user and token generated
            print(type(instance))
            token = Token.objects.get(user=instance)
            print(token)
            token_value = getattr(token, "key")
            print(token_value)
            return JsonResponse({'token': token_value}, status=201)

        else:
            print(serializer.errors)
            # Add custom message or error code in here?
            return HttpResponse(status=400)
