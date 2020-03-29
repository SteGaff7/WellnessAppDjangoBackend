from django.urls import path
from .views import Register, CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Only handles POST requests
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-login-token-auth/', CustomAuthToken.as_view(), name='api_login_token_auth'),
    path('register/', Register.as_view(), name='register'),
]