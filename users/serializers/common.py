from rest_framework import serializers
from teams.models import Team
from ..models import User
import urllib.parse

class AuthSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password_confirmation', 'job_title', 'profile_img', 'team']

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({'Password': 'Passwords do not match'})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        print('Validated:', validated_data)

        if not validated_data.get('profile_img'):
            username = validated_data.get('username', 'User')
            encoded_username = urllib.parse.quote(username)
            validated_data['profile_img'] = f"https://ui-avatars.com/api/?name={encoded_username}&background=6366f1&color=ffffff&size=200"


        return User.objects.create_user(**validated_data)

class OwnerSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), required=False, allow_null=True)
    team_info = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'job_title', 'profile_img', 'team', 'team_info']

    def get_team_info(self, obj):
        if obj.team:
            return {
                'id': obj.team.id,
                'name': obj.team.name
            }
        return None

