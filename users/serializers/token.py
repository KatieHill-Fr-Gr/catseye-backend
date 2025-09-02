from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user'] = {
            'id': user.id,
            'username': user.username,
            'profile_img': user.profile_img,
            'job_title': user.job_title, 
        }

        return token