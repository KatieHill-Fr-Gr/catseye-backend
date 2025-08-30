from rest_framework.serializers import ModelSerializer, FileField, ValidationError
from ..models import Termbase, Term

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['id', 'source_term', 'target_term', 'notes']

class TermbaseSerializer(ModelSerializer):
     terms = TermSerializer(many=True, read_only=True)

     class Meta:
            model = Termbase
            fields = ['id', 'name', 'created_by', 'source_language', 'target_language', 
                 'created_at', 'updated_at', 'terms']
