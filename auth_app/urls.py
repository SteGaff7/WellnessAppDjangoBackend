from django.urls import path
from .views import CheckAuth, Register
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('check_auth/', CheckAuth.as_view(), name="check-auth"),
    # Only handles POST requests
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', Register.as_view(), name='register'),
]