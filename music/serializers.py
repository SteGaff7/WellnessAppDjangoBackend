from rest_framework import serializers
from .models import Songs, Restaurant

# More on serializers
# https://www.django-rest-framework.org/api-guide/serializers/

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name','latitude','longitude','address')
