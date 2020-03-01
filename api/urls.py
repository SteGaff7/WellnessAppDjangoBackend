from django.urls import path
from .views import SendData, WellnessAPI

urlpatterns = [
    path('send_data/', SendData.as_view(), name="send-data"),
    path('wellness/', WellnessAPI.as_view(), name="wellness-data"),

]
