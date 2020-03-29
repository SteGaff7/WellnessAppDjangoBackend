from django.urls import path
from .views import Wellness

urlpatterns = [
    path('', Wellness.as_view(), name="wellness"),
]