from rest_framework.serializers import ModelSerializer, FileField, ValidationError
from ..models import Termbase

class TermbaseSerializer(ModelSerializer):     
     class Meta:
            model = Termbase
            fields = '__all__'
