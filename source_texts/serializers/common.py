from rest_framework.serializers import ModelSerializer, FileField, ValidationError
from ..models import Source

class SourceSerializer(ModelSerializer):
     source_file = FileField(write_only=True, required=False)
     
     class Meta:
            model = Source
            fields = ['id', 'title', 'body', 'source_language', 'source_file', 'feedback', 'parent_task']

     def validate(self, data):
        if not data.get('body') and not data.get('source_file'):
            raise ValidationError({'body': 'Please provide a text' })
        return data

     