from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Termbase
from .serializers.common import TermbaseSerializer
from .serializers.populated import PopulatedTermbaseSerializer
from rest_framework.exceptions import NotFound, PermissionDenied


# * Path: /termbases

class TermbaseListView(APIView):
    # Index route
    def get(self, request):
        termbases = Termbase.objects.all()
        serialized_termbases = PopulatedTermbaseSerializer(termbases, many=True)
        return Response(serialized_termbases.data)

    # Create route
    def post(self, request):
        serialized_termbases = TermbaseSerializer(data=request.data)
        serialized_termbases.is_valid(raise_exception=True)
        serialized_termbases.save(created_by=request.user)
        return Response(serialized_termbases.data, 201)
    

# * Path: /termbases/<int:pk>/

class TermbaseDetailView(APIView):

    # Object or 404
    def get_termbase(self, pk):
        try:
            return Termbase.objects.get(pk=pk)
        except Termbase.DoesNotExist as e:
            print(e)
            raise NotFound('Termbase does not exist.')  
        
    # Show route
    def get(self, request, pk):
        termbase = self.get_termbase(pk)
        serialized_termbase = PopulatedTermbaseSerializer(termbase)
        return Response(serialized_termbase.data)
        
    
    # Update route
    def put(self, request, pk):
        termbase = self.get_termbase(pk)

        serialized_termbase = TermbaseSerializer(termbase, data=request.data, partial=True)
        serialized_termbase.is_valid(raise_exception=True)
        serialized_termbase.save()
        return Response(serialized_termbase.data)
    
    # Delete route
    def delete(self, request, pk):
       termbase = self.get_termbase(pk)  
       termbase.delete()
       return Response(status=204)