from django.urls import path
from .views import SerializationAPI

urlpatterns = [
    path('serialization/', SerializationAPI.as_view(), name="serialization_api"),
]