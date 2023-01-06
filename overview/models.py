from django.db import models
from user.models import User
import uuid


class SexChoice(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'


class Overview(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    sex = models.CharField(max_length=6, choices=SexChoice.choices)

    height = models.DecimalField(max_digits=3, decimal_places=2)

    weight = models.DecimalField(max_digits=4, decimal_places=1)

    bmi = models.DecimalField(max_digits=4, decimal_places=2)

    whr = models.DecimalField(max_digits=3, decimal_places=2)

    lean_mass = models.DecimalField(max_digits=4, decimal_places=2)

    fat_mass = models.DecimalField(max_digits=4, decimal_places=2)

    body_fat = models.DecimalField(max_digits=4, decimal_places=2)

    created_at = models.DateField(auto_now_add=True)
    
    created_by = models.ForeignKey(User, 
        on_delete=models.CASCADE,
        related_name='owner_overview')

    student = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='overviews'
    )
