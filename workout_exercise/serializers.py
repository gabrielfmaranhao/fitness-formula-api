from rest_framework import serializers
from .models import Workout_exercise
from exercise.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
        read_only_fields = ["id"]


class Workout_exerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = Workout_exercise
        fields = ["id", "exercise", "equipment", "description", "sets", "reps"]
        read_only_fields = ["id", "workout", "exercise"]
