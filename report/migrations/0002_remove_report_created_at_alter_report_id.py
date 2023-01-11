# Generated by Django 4.1.5 on 2023-01-11 12:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="report",
            name="created_at",
        ),
        migrations.AlterField(
            model_name="report",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]