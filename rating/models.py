from django.db import models
import uuid

class RatingChoices(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
class Rating(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    comment = models.CharField(max_length=200)
    stars = models.PositiveSmallIntegerField(choices=RatingChoices.choices)

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
