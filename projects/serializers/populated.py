from .common import ProjectSerializer
from users.serializers.common import OwnerSerializer

class PopulatedProjectSerializer(ProjectSerializer):
    project_owner = OwnerSerializer()
