from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Project
from .serializers.common import ProjectSerializer
from .serializers.populated import PopulatedProjectSerializer

class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedProjectSerializer
        return ProjectSerializer 

class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedProjectSerializer 
        return ProjectSerializer

class UserTeamProjectsView(ListCreateAPIView):
    serializer_class = PopulatedProjectSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(team=user.team)