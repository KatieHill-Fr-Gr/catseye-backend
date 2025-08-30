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
      
      name = models.CharField(max_length=25)
      created_by = models.ForeignKey(to='users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='owned_termbases')
      source_language = models.CharField(max_length=25, choices=LANG_CHOICES, default='en-gb')
      target_language = models.CharField(max_length=25, choices=LANG_CHOICES, default='fr-FR')
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
    
      def __str__(self):
        return f"{self.name} ({self.source_language} → {self.target_language})"
    
class Term(models.Model):
    termbase = models.ForeignKey(Termbase, on_delete=models.CASCADE, related_name='terms')
    source_term = models.CharField(max_length=255)
    target_term = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True, help_text="Additional explanation of term")
    
    def __str__(self):
        return f"{self.source_term} → {self.target_term}"