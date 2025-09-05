from django.urls import path
from .views import SignUpView
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignUpView, UserUpdateView

urlpatterns = [
    path('sign-up/', SignUpView.as_view()),
    path ('sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('<int:user_id>/', UserUpdateView.as_view(), name='user-update'),
]