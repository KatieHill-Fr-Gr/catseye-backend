from .common import TaskSerializer
from users.serializers.common import OwnerSerializer
from source_texts.serializers.common import SourceSerializer
from translations.serializers.common import TranslationSerializer

class PopulatedTaskSerializer(TaskSerializer):
    assigned_to = OwnerSerializer()
    source_text = SourceSerializer()
    translation = TranslationSerializer()
    