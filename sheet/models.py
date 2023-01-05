from django.db import models
import uuid

# Create your models here.
class TrainingType(models.TextChoices):
    HYPERTROPHY = "hypertrophy"
    FAT_LOSS = "fat_loss"
    KEEP_IN_SHAPE = "keep_in_shape"
    BODYBUILDER = "bodybuilder"


class Sheet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.CharField(max_length=20, choices=TrainingType.choices)
    created_at = models.DateField(auto_now_add=True)
    until = models.DateField()

    trainer = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="trainer_sheets",
    )

    student = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        related_name="student_sheet",
    )
