from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import AuthSerializer
from rest_framework.permissions import AllowAny
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Sign-up

class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serialized_user = AuthSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        print(serialized_user.data)

        refresh = RefreshToken.for_user(serialized_user.instance)
        print('ACCESS TOKEN:', refresh.access_token)

        return Response({
            'refresh_token': str(refresh),
             'access_token': str(refresh.access_token)
            }, 201)


