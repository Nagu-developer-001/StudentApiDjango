from rest_framework import serializers
from .models import StudentDetails

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ['stid','st_name','program','st_cgpa','st_city']
