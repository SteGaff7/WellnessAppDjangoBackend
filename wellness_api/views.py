# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import json
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from wellness_api.models import WellnessEntry
from wellness_api.serializers import WellnessEntrySerializer


class Wellness(APIView):
    permission_classes = [IsAuthenticated]
    # Add Object level permissions
    # self.check_object_permissions(self.request, obj)

    def get(self, request):
        """
        Will handle single day requests and all entries etc.
        Return for graph and scroll view etc
        """
        return HttpResponse(status=200)

    def post(self, request):
        """
        Check if user is authenticated with token - done automatically
        Check if entry for date already exists - do separate request I think

        Edit entry possibility

        If valid then save data using serializers and return response to user

        Other permissions needed?
        """

        data = JSONParser().parse(request)
        serializer = WellnessEntrySerializer(data=data, context={'request': request})
        # print(data)

        if serializer.is_valid():
            # Could pass request.user here either and change user from read only
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            print(serializer.errors)
            return HttpResponse(status=400)

    def put(self, request):
        """
        Method for updating or changing existing entries
        """
        data = JSONParser().parse(request)

        # Error handle these?
        user = request.user
        date = data['date']

        try:
            # Get entry to be edited
            entry = WellnessEntry.objects.get(user=user, date=date)

            # Pass to serializer to call update method
            serializer = WellnessEntrySerializer(entry, data=data, context={'request': request})

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            else:
                print(serializer.errors)
                return HttpResponse(status=400)

        except Exception as e:
            print(e)
            return HttpResponse(status=400)