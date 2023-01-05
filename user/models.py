from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )
    middle_name = models.CharField(max_length=150, blank=True)
    birthdate = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
