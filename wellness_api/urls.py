from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import Wellness

urlpatterns = [
    path('', Wellness.as_view(), name="wellness"),
    path('<str:date>', Wellness.as_view(), name="wellness"),
]

urlpatterns = format_suffix_patterns(urlpatterns)