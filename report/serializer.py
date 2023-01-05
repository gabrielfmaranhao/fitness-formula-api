from rest_framework import serializers
from .models import Report
from user.models import User


class ReportSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(max_length=250)
    date = serializers.DateTimeField(auto_now_add=True)
    created_at = serializers.DateTimeField(auto_now_add=True)
    updated_at = serializers.DateTimeField(auto_now_add=True)
    id = serializers.IntegerField(read_only=True)
    

    # title = models.CharField()
    # description = models.CharField(max_length=250)
    # date = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    # trainer_id = models.ForeignKey(
    #     'trainers.Trainer',
    #     on_delete=models.CASCADE,
    #     related_name='report'
    # )

    # student_id = models.ForeignKey(
    #     'students.Student',
    #     on_delete=models.CASCADE,
    #     related_name='report'
    # )