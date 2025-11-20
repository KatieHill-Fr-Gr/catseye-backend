from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Translation
from .serializers.common import TranslationSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from .services.deepl_service import translate_text


# * Path: /translations

class TranslationListView(APIView):
    # Index route
    def get(self, request):
        translations = Translation.objects.all()
        serialized_translations = TranslationSerializer(translations, many=True)
        return Response(serialized_translations.data)

    # Create route
    def post(self, request):
        serialized_translations = TranslationSerializer(data=request.data)
        serialized_translations.is_valid(raise_exception=True)
        serialized_translations.save()
        return Response(serialized_translations.data, 201)
    

# * Path: /translations/<int:pk>/

class TranslationDetailView(APIView):
  
    # Object or 404
    def get_translation(self, pk):
        try:
            return Translation.objects.get(pk=pk)
        except Translation.DoesNotExist as e:
            print(e)
            raise NotFound('Translation does not exist.')  
        
    # Show route
    def get(self, request, pk):
        translation = self.get_translation(pk)
        serialized_translation = TranslationSerializer(translation)
        return Response(serialized_translation.data)
        
    
    # Update route
    def put(self, request, pk):
        translation = self.get_translation(pk)

        serialized_translation = TranslationSerializer(translation, data=request.data, partial=True)
        serialized_translation.is_valid(raise_exception=True)
        serialized_translation.save()
        return Response(serialized_translation.validated_data)
    
    # Delete route
    def delete(self, request, pk):
        translation = self.get_translation(pk)  

        translation.delete()
        return Response(status=204)
    
# * Path: translations/auto-translate/

class AutoTranslateView(APIView):
    def post(self, request):
        source_text = request.data.get('text')
        target_lang = request.data.get('target_lang')

        if not source_text or not target_lang:
            return Response(
                {'error': 'Missing text or target-lang'},
                 status=400
            )

        translated = translate_text(source_text, target_lang)
        return Response({'translated_text': translated})
