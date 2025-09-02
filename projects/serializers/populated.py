from .common import ProjectSerializer
from users.serializers.common import OwnerSerializer
from teams.serializers.common import TeamSerializer

class PopulatedProjectSerializer(ProjectSerializer):
    owner = OwnerSerializer()
    team = TeamSerializer()

    class Meta(ProjectSerializer.Meta):
        fields = ['id', 'name', 'brief', 'deadline', 'images', 'status', 'owner', 'team']
