from rest_framework.serializers import ModelSerializer
from ..models import Project

class ProjectSerializer(ModelSerializer):
     class Meta:
            model = Project
            fields = ['name', 'brief', 'deadline', 'images']

     def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        validated_data['team'] = user.team
        return super().create(validated_data)