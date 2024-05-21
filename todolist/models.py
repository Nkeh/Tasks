from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]
        #verbose_name = 'Task'
