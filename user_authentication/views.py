from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from user_authentication.serializers import UserSerializer

from wellness_api.models import WellnessEntry


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


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        # Get last_wellness_date to return
        try:
            wellness_instance = WellnessEntry.objects.filter(user=user).order_by("-date")[0]
            last_wellness_date = getattr(wellness_instance, "date")
        except IndexError as e:
            last_wellness_date = None
        print(last_wellness_date)
        return Response({
            'token': token.key,
            'date': last_wellness_date
        })
