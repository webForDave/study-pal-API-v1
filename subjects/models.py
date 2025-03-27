from django.db import models
from django.contrib.auth import get_user_model

class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    credits_load = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
