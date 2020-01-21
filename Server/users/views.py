from django.shortcuts import render

# Create your views here.
from rest_framework_jwt.views import ObtainJSONWebToken

from Server.users.custom_auth import JWTSerializer


class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer
