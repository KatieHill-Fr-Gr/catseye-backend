from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Source

from .serializers.common import SourceSerializer

from rest_framework.exceptions import NotFound, PermissionDenied
# ? from rest_framework.permissions import IsAuthenticatedOrReadOnly

# * Path: /source_texts

class SourceListView(APIView):
    # ? permission_classes = [IsAuthenticatedOrReadOnly]

    # Index route
    def get(self, request):
        source_texts = Source.objects.all()
        serialized_source_texts = SourceSerializer(source_texts, many=True)
        return Response(serialized_source_texts.data)

    # Create route
    def post(self, request):
        serialized_source_texts = SourceSerializer(data=request.data)
        serialized_source_texts.is_valid(raise_exception=True)

        source_file = serialized_source_texts.validated_data.get('source_file')
        file_data = None
        if source_file:
            file_data = source_file.read().decode('utf-8')
        
        if serialized_source_texts.validated_data.get('source_file'):
            serialized_source_texts.validated_data.pop('source_file')

        if file_data:
            serialized_source_texts.save(body=file_data)
        else: 
            serialized_source_texts.save()
        
        return Response(serialized_source_texts.data, 201)
    

# * Path: /source_texts/<int:pk>/

class SourceDetailView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # object or 404
    def get_source(self, pk):
        try:
            return Source.objects.get(pk=pk)
        except Source.DoesNotExist as e:
            print(e)
            raise NotFound('Source text does not exist.')  
        
    # Show route
    def get(self, request, pk):
        source_text = self.get_source(pk)
        serialized_source_text = SourceSerializer(source_text)
        return Response(serialized_source_text.data)
        
    
    # Update route
    def put(self, request, pk):
        source_text = self.get_source(pk)
        serialized_source_text = SourceSerializer(source_text, data=request.data, partial=True)
        serialized_source_text.is_valid(raise_exception=True)
        serialized_source_text.save()
        return Response(serialized_source_text.validated_data)
    
    # Delete route
    def delete(self, request, pk):
        source_text = self.get_source(pk)    
        source_text.delete()
        return Response(status=204)



