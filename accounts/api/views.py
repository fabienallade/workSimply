from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from accounts.api.utils import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class AuthView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, **kwargs):
        if request.user.is_authenticated():
            return Response({'details': 'You are already authentificated'}, status=200)
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({'token': token})


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, **kwargs):
        if request.user is not None:
            if request.user.is_authenticated:
                return Response({'details': 'You are already authentificated'})
        data = request.data

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        password2 = data.get('password2')

        if username is None:
            return Response({"details":"le parametre username est requis"})
        if email is None:
            return Response({"details":"le parametre email est requis"})
        if password is None:
            return Response({"details":"le parametre password est requis"})
        if password2 is None:
            return Response({"details":"le parametre password2 est requis"})

        qs = User.objects.filter(
            Q(username__iexact=username),
            Q(email__iexact=email)
        )
        if qs.exists():
            return Response({'details': 'user already exist'})
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = jwt_response_payload_handler(token, user, request=request)
            return Response(response)
        return Response({'details': 'Bad request'}, status=400)
