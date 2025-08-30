from django.db import models

class Termbase(models.Model):

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
      
      created_by = models.ForeignKey(to='users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='owned_termbases')
      source_language = models.CharField(max_length=25, choices=LANG_CHOICES, default='en-gb')
      target_language = models.CharField(max_length=25, choices=LANG_CHOICES, default='fr-FR')
     