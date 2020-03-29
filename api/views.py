# # from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from rest_framework import status
# from rest_framework.parsers import JSONParser
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
# import json
#
# from django.contrib.auth.models import User
# # from api.models import WellnessEntry, TestOwner
# from api.serializers import WellnessEntrySerializer, TestOwnerSerializer, UserSerializer
# from datetime import date
#
#
# # Create your views here.
#
# class WellnessAPI(APIView):
#
#     def get(self, request):
#         """
#         Test view that will return all wellness entries to the user as JSON
#         """
#
#         # Consider reimplementing with url configuration/regex instead of queries
#
#         # Django recognizes request parameters by ?user=7 etc
#         # print(request.GET.get('user', 'not found'))
#         # print(request.GET['user'])
#
#         # Request.GET returns QueryDict where there may be multiple values for key
#         print(request.GET)
#         if request.GET.get('user'):
#             # Get user specified
#             # Use JSON Response
#             return HttpResponse(json.dumps([{'test': 1}]), status=200)
#
#         else:
#             # Retrieve all data
#
#             # Queryset
#             entries = WellnessEntry.objects.all()
#             serializer = WellnessEntrySerializer(entries, many=True)
#
#             # JSONResponse subclass of HttpResponse, has a json encoder and it
#             # will check that format is valid, sets content type to json
#
#             # Use safe=True if sending dicts
#             return JsonResponse(serializer.data, safe=False, status=200)
#
#     def post(self, request):
#
#         data = JSONParser().parse(request)
#         print(data)
#         print()
#         serializer = WellnessEntrySerializer(data=data)
#
#         # Add check that user and date don't already exist and if so custom error that
#         # Android app can use to display Toast message
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#
#         return HttpResponse(serializer.errors, status=400)
#
#
# class UserAPI(APIView):
#     def post(self, request):
#         data = JSONParser().parse(request)
#         print(data)
#
#         user_id = data['owner']['username']
#         text = data['text']
#         user = User.objects.get_by_natural_key(user_id)
#
#         # t = TestOwner(owner=user, text="this is  more text")
#         # t.save()
#
#
#         data = {'owner': user, 'text': text}
#
#         print(data)
#
#         serializer = TestOwnerSerializer(data=data)
#         # serializer = UserSerializer(data=data)
#
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             # serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         else:
#             print("No")
#         print(serializer.error_messages)
#         return HttpResponse(serializer.errors, status=400)
#
#         # return HttpResponse(status=200)
#
#
#         # print(type(user))
#         # print(user)
#
#         # if request.data['user']:
#         #     print("Found")
#
#         # return HttpResponse(status=200)
#
#         # data = JSONParser().parse(request)
#         # print(data)
#         # print()
#         # serializer = TestOwnerSerializer(data=data)
#         #
#         # if serializer.is_valid():
#         #     print("valid")
#         #     print(serializer.validated_data)
#         #     return JsonResponse(serializer.data, status=201)
#         #
#         # return HttpResponse(serializer.errors, status=400)
#
#
#
#
# class SendData(APIView):
#
#     # def get(self, request, format=None):
#     #     x = {"name" : "stephen"}
#     #     ser = json.dumps(x)
#     #
#     #     # If using response then it must be serialized
#     #     return Response(ser, status=status.HTTP_200_OK)
#     #     # return HttpResponse(ser, status=status.HTTP_200_OK)
#
#     def get(self, request, format=None):
#         # format allows different urls such as user.json and user.html
#         # without having to create 2 different url patterns
#
#         '''
#         Create entry with following data, save to DB then use serializer to
#         retrieve data before converting it to JSON
#         Return the JSON with status code as response
#         '''
#         entry = WellnessEntry(user=1,
#                               date=date.today(),
#                               sleep_score=3,
#                               energy_score=4,
#                               soreness_score=4,
#                               stress_score=2,
#                               mood_score=4,
#                               total_score=17)
#         entry.save()
#         serializer = WellnessEntrySerializer(entry)
#         data = serializer.data
#
#         content = JSONRenderer().render(data)
#
#         # If using Response (Django Rest) then pass it Python primitives and
#         # not rendered content
#
#         # HttpResponse requires you to serialize data to JSON as above
#         return HttpResponse(content, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         data = request.data
#         for key in data:
#             print(data[key])
#         # print(data)
#
#         # Can send a message response but will need to be in JSON for android app
#         return Response("message", status=status.HTTP_200_OK)
