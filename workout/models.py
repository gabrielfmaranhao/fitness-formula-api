from django.db import models
import uuid


class MuscleChoices(models.TextChoices):
    CHOICES_LEGS = "legs"
    CHOICES_ARMS = "arms"
    CHOICES_BACK = "back"
    CHOICES_CHEST = "chest"
    CHOICES_SHOLDERS = "shoulders"
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
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    muscle_group = models.CharField(choices=MuscleChoices.choices, max_length=10)
    day = models.CharField(choices=DayChoices.choices, max_length=10)
    title = models.CharField(null=True, max_length=120)
    description = models.TextField(null=True)
    sheet = models.ForeignKey(
        "sheet.Sheet", on_delete=models.CASCADE, related_name="sheet"
    )
