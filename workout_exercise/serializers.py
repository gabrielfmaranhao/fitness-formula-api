from rest_framework import serializers
from .models import Exercise, Workout_exercise

class Workout_exerciseSerializer(serializers.ModelSerializer):
    class Meta():
        model = Workout_exercise
        fields = '__all__'
        read_only_fields = ['id']
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta():
        model = Exercise
        fields = '__all__'
        read_only_fields = ['id']