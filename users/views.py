from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers.common import AuthSerializer
from .models import User

# * Path: /users/sign-up

class SignUpView(APIView):

    def post(self, request):
        return Response("Hit sign-up view")


