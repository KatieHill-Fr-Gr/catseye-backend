from django.urls import path
from translations.views import TranslationListView, TranslationDetailView

urlpatterns = [
    path('', TranslationListView.as_view()),
    path('<int:pk>/', TranslationDetailView.as_view())
]