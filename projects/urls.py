from django.urls import path
from projects.views import ProjectListView
from projects.views import ProjectDetailView
from projects.views import UserTeamProjectsView
from tasks.views import TaskListView, TaskDetailView 


urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<int:pk>/', ProjectDetailView.as_view()),
    path('<int:pk>/tasks/', TaskListView.as_view()),
    path('<int:pk>/tasks/<int:task_pk>/', TaskDetailView.as_view()),
    path('user-team-projects/', UserTeamProjectsView.as_view()),
]
