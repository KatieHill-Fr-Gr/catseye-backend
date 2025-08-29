from rest_framework.serializers import ModelSerializer
from ..models import Source

class SourceSerializer(ModelSerializer):
     class Meta:
            model = Source
            fields = '__all__'