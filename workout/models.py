from django.db import models

class MuscleChoices(models.TextChoices):
    CHOICES_LEGS = "legs"
    CHOICES_ARMS = "arms"
    CHOICES_BACK = "back"
    CHOICES_CHEST = "chest"
    CHOICES_SHOLDERS = "sholders"
    CHOICES_CARDIO = "cardio"
class DayChoices(models.TextChoices):
    CHOICES_MONDAY = "monday"
    CHOICES_TUESDAY = "tuesday"
    CHOICES_WEDNESDAY = "wednesday"
    CHOICES_THURSDAY = "thursday"
    CHOICES_FRIDAY = "friday"
    CHOICES_SATURDAY = "saturday"
    CHOICES_SUNDAY = "sunday"
class Workout(models.Model):
    id = models.UUIDField(primary_key=True)
    muscle_group = models.CharField(choices=MuscleChoices.choices)
    day = models.CharField(choices=DayChoices.choices)
    title = models.CharField(null=True)
    description = models.CharField(null=True)
    sheet = models.ForeignKey('sheet.Sheet', on_delete=models.CASCADE, related_name="workouts")
