from django.urls import path
from termbases.views import TermbaseListView, TermbaseDetailView, TermListView

urlpatterns = [
    path('', TermbaseListView.as_view()),
    path('<int:pk>/', TermbaseDetailView.as_view()),
    path('<int:termbase_pk>/terms/', TermListView.as_view())
]