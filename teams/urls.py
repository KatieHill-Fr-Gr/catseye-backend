from django.urls import path
from .views import TeamsListView

urlpatterns = [
    path('', TeamsListView.as_view(), name='teams-list'),
]