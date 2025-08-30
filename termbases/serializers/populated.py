from .common import TermbaseSerializer
from users.serializers.common import OwnerSerializer

class PopulatedTermbaseSerializer(TermbaseSerializer):
    created_by = OwnerSerializer()