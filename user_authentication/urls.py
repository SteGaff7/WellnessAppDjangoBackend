from django.urls import path
from .views import Register
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Only handles POST requests
    path('users/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('users/register/', Register.as_view(), name='register'),
]