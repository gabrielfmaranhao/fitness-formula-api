from django.db import models
import uuid


class Workout_exercise(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    equipment = models.CharField(null=True, max_length=120)
    description = models.TextField(null=True)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    workout = models.ForeignKey(
        "workout.Workout",
        on_delete=models.CASCADE,
        related_name="exercises",
    )
    exercise = models.ForeignKey(
        "exercise.Exercise",
        on_delete=models.CASCADE,
        related_name="workouts",
    )
