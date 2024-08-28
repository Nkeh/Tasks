from django.db import models
from django.contrib.auth.models import User

import os


# Create your models here.
def user_directory_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', unique=True)
    img = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'