from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField


class Source(models.Model):
    # parent_task = models.ForeignKey(to='tasks.Task', on_delete=models.SET_NULL, null=True, blank=True, related_name='task_source_texts')

    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    source_language = models.CharField(max_length=50)
    feedback = ArrayField(models.JSONField(default=dict), default=list, blank=True)

  
    
    

