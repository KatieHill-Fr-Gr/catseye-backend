from rest_framework.generics import ListCreateAPIView
from .models import Team
from .serializers.common import TeamSerializer

class TeamsListView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer