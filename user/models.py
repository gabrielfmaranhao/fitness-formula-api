from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True)
    birthdate = models.DateField()
    cpf = models.CharField(max_length=11)
