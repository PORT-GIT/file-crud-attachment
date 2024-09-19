from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import viewsets
#it is a view provide by DRF that automatically handles CRUD operations
#foregoing the need to write separate code
from .models import Filelog, Filemovement
from .serializers import FilelogSerializer, FilemovementSerializer

# Create your views here.

class FileLogViewSet(viewsets.ModelViewSet):
    queryset = Filelog.objects.all()
    serializer_class = FilelogSerializer

class FilemovementViewSet(viewsets.ModelViewSet):
    queryset = Filemovement.objects.all()
    serializer_class = FilemovementSerializer
