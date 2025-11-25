from django.urls import path
from translations.views import TranslationListView, TranslationDetailView, AutoTranslateView

urlpatterns = [
    path('', TranslationListView.as_view()),
    path('<int:pk>/', TranslationDetailView.as_view()),
    path('auto-translate/', AutoTranslateView.as_view())
]