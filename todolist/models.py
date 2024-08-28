from django.db import models
from users.models import Profile
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    atachment = models.FileField(upload_to="media/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')



    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]
        verbose_name = 'task'
