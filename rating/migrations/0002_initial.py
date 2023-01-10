# Generated by Django 4.1.5 on 2023-01-09 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rating", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_ratings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="rating",
            name="trainer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trainer_ratings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
