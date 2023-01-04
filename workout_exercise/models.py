from django.db import models
import uuid
class Workout_exercise(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    equipment = models.CharField(null=True)
    description = models.CharField(null=True)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    workout = models.ForeignKey('workout.Workout', on_delete=models.CASCADE, related_name="workout_exercises")
    exercise = models.ForeignKey('workout_exercise.Exercise', on_delete=models.CASCADE, related_name="workout_exercises")

class Exercise(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField()
