from django.shortcuts import render
# from django.http import HttpResponse
from .models import Filelog, Filemovement
from .serializers import FilelogSerializer, FilemovementSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Filelog, Filemovement
from .serializers import FilelogSerializer, FilemovementSerializer

# List all file logs and allow creation
class FilelogListView(generics.ListCreateAPIView):
    queryset = Filelog.objects.all()
    serializer_class = FilelogSerializer

    def post(self, request, *args, **kwargs):
        # Check for duplicate classification before creating
        classification = request.data.get('classification')
        if Filelog.objects.filter(classification=classification).exists():
            return Response({"error": "File with this classification already exists."}, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)

# To retrieve, update or delete a file log
class FilelogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filelog.objects.all()
    serializer_class = FilelogSerializer

# To track file movement 
class FileMovementView(generics.ListCreateAPIView):
    queryset = Filemovement.objects.all()
    serializer_class = FilemovementSerializer

# Search files by classification or name
class SearchFileView(generics.ListAPIView):
    serializer_class = FilelogSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Filelog.objects.filter(name__icontains=query) | Filelog.objects.filter(classification__icontains=query)
