from django.db import models
from django.contrib.postgres.fields import ArrayField


class Translation(models.Model):

    LANG_CHOICES = [
        ('en-GB', 'English (UK)'),
        ('en-US', 'English (US)'),
        ('fr-FR', 'French'),
        ('es-ES', 'Spanish'),
        ('it-IT', 'Italian'),
        ('gr-GR', 'Greek'),
        ('de-DE', 'German'),
        ('nl-NL', 'Dutch'),
        ('pl-PL', 'Polish'),
    ]

    title = models.CharField(max_length=255)
    body = models.JSONField(blank=True, null=True)
    target_language = models.CharField(max_length=25, choices=LANG_CHOICES, default='en-GB')
    source_text = models.ForeignKey(to='source_texts.Source', on_delete=models.CASCADE, null=True, blank=True, related_name='translations')
    termbase = models.ForeignKey(to='termbases.Termbase', on_delete=models.SET_NULL, null=True, blank=True, related_name='translations')

    feedback = ArrayField(models.JSONField(default=dict), default=list, blank=True)
