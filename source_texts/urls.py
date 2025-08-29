from django.urls import path
from source_texts.views import SourceListView, SourceDetailView

urlpatterns = [
    path('', SourceListView.as_view()),
    path('<int:pk>/', SourceDetailView.as_view())
]