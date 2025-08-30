from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Translation

from .serializers.common import TranslationSerializer

from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated

# * Path: /translations

class TranslationListView(APIView):
    permission_classes = IsAuthenticated

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
    permission_classes = IsAuthenticated

    # Object or 404
    def get_translation(self, pk):
        try:
            return Translation.objects.get(pk=pk)
        except Translation.DoesNotExist as e:
            print(e)
            raise NotFound('Translation does not exist.')  
        
    # Show route
    def get(self, request, pk):
        translation = self.get_source(pk)
        serialized_translation = TranslationSerializer(translation)
        return Response(serialized_translation.data)
        
    
    # Update route
    def put(self, request, pk):
        translation = self.get_translation(pk)

        # if project.team does not include request.user:
        #     raise PermissionDenied() 

        serialized_translation = TranslationSerializer(translation, data=request.data, partial=True)
        serialized_translation.is_valid(raise_exception=True)
        serialized_translation.save()
        return Response(serialized_translation.validated_data)
    
    # Delete route
    def delete(self, request, pk):
        translation = self.translation(pk)  

        # if project.team does not include request.user:
        #     raise PermissionDenied() 

        translation.delete()
        return Response(status=204)