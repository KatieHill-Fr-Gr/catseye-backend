from django.urls import path
from termbases.views import TermbaseListView, TermbaseDetailView

urlpatterns = [
    path('', TermbaseListView.as_view()),
    path('<int:pk>/', TermbaseDetailView.as_view())
]