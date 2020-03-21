from django.http import HttpResponse, JsonResponse
from rest_framework.exceptions import ValidationError
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

        # try:
        #     serializer.is_valid()
        #     print("here")
        # except ValidationError as e:
        #     print("caught")
        #     print(e)
        #
        # return HttpResponse(status=400)

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
