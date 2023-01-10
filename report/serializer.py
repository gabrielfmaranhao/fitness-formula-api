from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
            model = Report
            fields = [
            "id",
            "title",
            "description",
            "date",
            "created_at",
            "updated_at",
            "trainer_name",
            "trainer",
            "student_name",
            "student",
        ]
            read_only_fields = ['id', 'trainer', 'student']
    
    student_name = serializers.SerializerMethodField()
    trainer_name = serializers.SerializerMethodField()

    def get_student_name(self, obj: Report):
        return obj.student.first_name + ' ' + obj.student.last_name

    def get_trainer_name(self, obj: Report):
        return obj.trainer.first_name + ' ' + obj.trainer.last_name

    def create(self, validated_data):
        return Report.objects.create(**validated_data)
    
