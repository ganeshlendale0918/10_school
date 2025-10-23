from rest_framework import serializers
from.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Students 
        fields='_all_'