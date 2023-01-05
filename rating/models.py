from django.db import models
import uuid


class Rating(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    comment = models.CharField(max_length=200)
    stars = models.PositiveSmallIntegerField()

    student = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="student_ratings",
    )

    trainer = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="trainer_ratings",
    )
