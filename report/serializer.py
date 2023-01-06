from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.Serializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ['trainer_id', 'student_id']

    def create(self, validated_data):
        return Report.objects.create(**validated_data)
    
   