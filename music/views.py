from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Songs, Restaurant
from .serializers import SongsSerializer, RestaurantSerializer

# Create your views here.

# Following this tutorial:
# https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5
# Authentication
# https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-part-2-cfb87e2c8a6c

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

class RestaurantList(APIView):
    """docstring for RestaurantList.

    If using APIView then must declare a get method
    """

    #queryset = Restaurant.objects.all()
    #serializer_class = RestaurantSerializer

    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
