from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'profile_img': user.profile_img,
            'job_title': user.job_title,
            'team': {
                'id': user.team.id if user.team else None,
                'name': user.team.name if user.team else None,
            }
        }
        return token