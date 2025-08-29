from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField


class Source(models.Model):

    LANG_CHOICES = [
        ('en-gb', 'English (UK)'),
        ('en-us', 'English (US)'),
        ('fr-fr', 'French'),
        ('es-es', 'Spanish'),
        ('it-it', 'Italian'),
        ('de-de', 'German'),
    ]

    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    source_language = models.CharField(max_length=25, choices=LANG_CHOICES, default='en-gb')
    feedback = ArrayField(models.JSONField(default=dict), default=list, blank=True)

  
    
    

