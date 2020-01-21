from abc import ABC

from Server.users.models import User
from django.utils.translation import ugettext as _
from rest_framework.authentication import BaseAuthentication
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler
from django.db.models import Q


class JWTSerializer(JSONWebTokenSerializer):
    def update(self, instance, validated_data):
        super(self)

    def create(self, validated_data):
        super(self)

    def validate(self, attrs):
        credentials = {
            'request': attrs,
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = CustomAuth().authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = _('La cuenta de usuario esta deshabilitada.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = _('No se puede iniciar sesión con las credenciales proporcionadas.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Debe incluir "{username_field}" y "contraseña".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)


class CustomAuth(BaseAuthentication):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
