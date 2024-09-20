# this serializer will convert django models data to JSON data and vice versa

from rest_framework import serializers
from .models import Filelog, Filemovement

class FilelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filelog
        fields = '__all__'
        

class FilemovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filemovement
        fields = ('file', 
                  'name_of_holder', 
                  'location_of_holder', 
                  'date_received')