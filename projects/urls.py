from django.urls import path
from projects.views import ProjectListView
from projects.views import ProjectDetailView


urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<int:pk>/', ProjectDetailView.as_view())
]
