from datetime import datetime
from rest_framework import serializers
from user.serializers import UserSerializer, TrainerSerializer
from .models import Sheet
import ipdb


class SheetSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    trainer_name = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()

    def get_student_name(self, obj: Sheet):
        return f"{obj.student.first_name} {obj.student.last_name}"

    def get_trainer_name(self, obj: Sheet):
        return f"{obj.trainer.first_name} {obj.trainer.last_name}"

    def get_duration(self, obj: Sheet):
        delta = obj.until - obj.created_at
        return f"{delta.days} days"

    class Meta:
        model = Sheet
        fields = [
            "id",
            "type",
            "created_at",
            "until",
            "duration",
            "trainer",
            "trainer_name",
            "student",
            "student_name",
        ]
        read_only_fields = [
            "trainer",
            "student",
        ]
