from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

from practice_serialization.models import SimpleObj
from practice_serialization.serializers import CommentSerializer, SimpleObjSerializer, ObjCreatedByUserSerializer


# Create your views here.


class SerializationAPI(APIView):

    def get(self, request):

        return HttpResponse("Hello world", status=200)

    def post(self, request):

        data = JSONParser().parse(request)
        print(data)

        try:
            # user = User.objects.get(username=data.pop("username"))
            print(data)
            serializer = ObjCreatedByUserSerializer(data=data)

            if serializer.is_valid():
                #  Can pass string in and find user or pass user object in
                serializer.save(username=data.pop("username"))
                return JsonResponse(serializer.data, status=201)
            else:
                print(serializer.errors)
                return HttpResponse(status=400)
        except:
            return HttpResponse(status=400)






        # try:
        #     instance = SimpleObj.objects.get(pk=data['my_id'])
        #     print(instance)
        #     # This will cause and update as instance passed to save method
        #     serializer = SimpleObjSerializer(instance, data=data)
        # except:
        # serializer = SimpleObjSerializer(data=data)
        #
        # # Return a 400 response if the data was invalid.
        # # if serializer.is_valid(raise_exception=True):
        # if serializer.is_valid():
        #     print(serializer.validated_data)
        #     serializer.save(another_field="this was passed at save()")
        #     return JsonResponse(serializer.data, status=201)
        #
        # print("No")
        # print(serializer.error_messages)
        # print(serializer.errors)
        # return HttpResponse(serializer.errors, status=400)

