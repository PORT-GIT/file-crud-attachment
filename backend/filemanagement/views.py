from django.shortcuts import render
# from django.http import HttpResponse
from .models import Filelog, Filemovement
from .serializers import FilelogSerializer, FilemovementSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FilelogSerializer, FilemovementSerializer
#these libraries are to analyze and extract info from documents(MS word and access)
import docx
import pyodbc

from django.http import JsonResponse
from .utils import extract_text_from_word  # assuming the function is in utils.py

# THIS WILL ALLOW THE CREATION AND LISTING OF THE FILES
class FilelogListView(generics.ListCreateAPIView):
    queryset = Filelog.objects.all()  
    # Shows all the file logs currently stored in the system
    serializer_class = FilelogSerializer
    
    def post(self, request, *args, **kwargs):
        classification = request.data.get('classification')
        name_of_file = request.data.get('name_of_file')
        
        # Check if a file with the same classification exists
        if Filelog.objects.filter(classification=classification).exists():
            return Response({"error": "File with this classification number already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if a file with the same name exists
        if Filelog.objects.filter(name_of_file=name_of_file).exists():
            return Response({"error": "File with this name already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no duplicates, it will proceed with creation
        return super().post(request, *args, **kwargs)


# THIS WILL ALLOW RETRIEVAL, UPDATES AND DELETION OF FILE LOGS
class FilelogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filelog.objects.all()
    serializer_class = FilelogSerializer


# TO TRACK FILE MOVEMENT 
class FilemovementView(generics.ListCreateAPIView):
    queryset = Filemovement.objects.all()
    serializer_class = FilemovementSerializer
# This view manages file movements, which is all about tracking where a file is and who has it. 


# TO SEARCH FOR FILES
class FileLogSearch(generics.ListAPIView):
    serializer_class = FilelogSerializer

    def get_queryset(self):
        queryset = Filelog.objects.all()
        classification = self.request.query_params.get('classification', None)
        name_of_file = self.request.query_params.get('name_of_file', None)
        if classification:
            queryset = queryset.filter(classification__icontains=classification)
        if name_of_file:
            queryset = queryset.filter(name_of_file__icontains=name_of_file)
        return queryset
# This view allows you to search for files in the system by their classification number or name.
#For searching, you can build a search API in Django using query parameters    

#The opened field in the Filelog model can be used to track whether a file has been opened.
class FileClosedView(APIView):
    def post(self, request, pk):
        try:
            filelog = Filelog.objects.get(pk=pk)
            filelog.closed = False
            filelog.save()
            return Response({"message": "File marked as opened."}, status=status.HTTP_200_OK)
        
        except Filelog.DoesNotExist:
            return Response({"error": "File is marked as closed."}, status=status.HTTP_404_NOT_FOUND)
        

#TO ANALYZE SOFT-COPY DOCUMENTS TO EXTRACT INFORMATION
#these functions will extract details which can auto-fill fields in the FileLog model.
def analyze_word_file(file_path):
    doc = docx.Document(file_path)
    data = {}
    for paragraph in doc.paragraphs:
        # Extract classification and movement data from the document
        if "Classification:" in paragraph.text:
            data['classification'] = paragraph.text.split(":")[1].strip()
        if "Movement:" in paragraph.text:
            data['movement'] = paragraph.text.split(":")[1].strip()
    return data


def extract_data_from_access(db_path):
    conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_path + ';'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM YourTable")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


def upload_document(request):
    #This view handles file uploads. 
    # It extracts text from a word file and attempts to determine its classification.

    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        text_content = extract_text_from_word(file.temporary_file_path())  # Extract text
        # Perform analysis or extraction of classification number from text_content
        classification = extract_text_from_word(text_content)
        return JsonResponse({'classification': classification})



