from django.db import models

class Workout_exercise(models.Model):
    id = models.UUIDField()
    equipment = models.CharField(null=True)
    description = models.CharField(null=True)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    workout = models.ForeignKey('workout.Workout', on_delete=models.CASCADE, related_name="workout_exercises")
    exercise = models.ForeignKey('workout_exercise.Exercise', on_delete=models.CASCADE, related_name="workout_exercises")

class Exercise(models.Model):
    id = models.UUIDField()
    title = models.CharField()
