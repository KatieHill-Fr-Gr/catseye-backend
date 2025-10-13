from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Project
from tasks.models import Task
from users.models import User
from .serializers.common import ProjectSerializer
from .serializers.populated import PopulatedProjectSerializer
from tasks.serializers.populated import PopulatedTaskSerializer
from users.serializers.common import OwnerSerializer

class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.select_related('team', 'owner').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedProjectSerializer
        return ProjectSerializer 

class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.select_related('team', 'owner').all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedProjectSerializer 
        return ProjectSerializer
    
class ProjectTeamUsersView(ListCreateAPIView):
    serializer_class = OwnerSerializer
    
    def get_queryset(self):
        project_id = self.kwargs.get('pk')
        project = Project.objects.select_related('team').filter(pk=project_id).first()
        if project:
            return User.objects.filter(team=project.team)
        return User.objects.none()
      

class UserTeamProjectsView(ListCreateAPIView):
    serializer_class = PopulatedProjectSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Project.objects.select_related('team', 'owner').filter(team_id=user.team.id)
    
class UserTasksView(ListCreateAPIView):
    serializer_class = PopulatedTaskSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Task.objects.select_related(
            'parent_project', 'assigned_to', 'source_text', 'translation').filter(assigned_to=user)