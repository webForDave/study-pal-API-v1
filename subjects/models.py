from django.db import models
from django.conf import settings

class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    credit_units = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
