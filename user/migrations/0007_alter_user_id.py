# Generated by Django 4.1.5 on 2023-01-05 14:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("d04a8983-0ed6-4b4e-a894-3238736c2329"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]