from .common import ProjectSerializer
from users.serializers.common import OwnerSerializer
from teams.serializers.common import TeamSerializer

class PopulatedProjectSerializer(ProjectSerializer):
    owner = OwnerSerializer()
    team = TeamSerializer()
