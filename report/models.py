from django.db import models
import uuid
class Report(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    trainer = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='created_report'
    )

    student = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='received_report'
    )