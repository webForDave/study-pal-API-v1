from django.db import models

class Goal(models.Model):

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High")
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    priority = models.CharField(max_length=8, choices=PRIORITY_CHOICES, default="medium")

    def __str__(self):
        return self.title