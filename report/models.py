from django.db import models

# Create your models here.

class Report(models.Model):
    title = models.CharField()
    description = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    trainer_id = models.ForeignKey(
        'trainers.Trainer',
        on_delete=models.CASCADE,
        related_name='report'
    )

    student_id = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='report'
    )