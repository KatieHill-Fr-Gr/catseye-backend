from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import AuthSerializer
from .serializers.common import OwnerSerializer
from .serializers.token import TokenSerializer
from rest_framework.permissions import AllowAny
from .models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Sign-up

class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serialized_user = AuthSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        print(serialized_user.data)

        refresh = TokenSerializer.get_token(serialized_user.instance)

        return Response({
             'access': str(refresh.access_token)
            }, 201)


class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]  # only logged-in users can update

    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OwnerSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)