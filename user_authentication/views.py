from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from user_authentication.serializers import UserSerializer


class Register(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        print(data)

        # Serialize data into user
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            instance = serializer.save()

            # Try obtain auth token here and return it after user and token generated
            token = Token.objects.get(user=instance)
            # token is a Token instance
            token_value = getattr(token, "key")

            return JsonResponse({'token': token_value}, status=201)
        else:
            # Not sure how to handle errors here yet
            # print(serializer.errors['password'][0])
            print(serializer.errors['password'])
            # Add custom message or error code in here?
            # 409 Conflict for existing user
            return HttpResponse(serializer.errors, status=400)
