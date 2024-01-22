from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields if needed
    pass

class UserScore(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.score}'
