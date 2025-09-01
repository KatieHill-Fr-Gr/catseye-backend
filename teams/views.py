from rest_framework.generics import ListCreateAPIView
from .models import Team
from .serializers.common import TeamSerializer
from rest_framework.permissions import AllowAny

class TeamsListView(ListCreateAPIView):
    permission_classes = [AllowAny] 
    queryset = Team.objects.all()
    serializer_class = TeamSerializer