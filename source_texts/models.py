from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField


class Source(models.Model):
    parent_task = models.ForeignKey(to='tasks.Task', on_delete=models.SET_NULL, null=True, blank=True, related_name='task_source_texts')

    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    source_file = models.FileField(upload_to='uploads/', blank=True, null=True)
    source_language = models.CharField(max_length=50)
    feedback = ArrayField(models.JSONField(default=dict), default=list, blank=True)

    def check_text(self):
        if not self.title and not self.body and not self.source_file:
            raise ValidationError('Please upload a file or provide your text directly in the fields provided.')
        
    def get_text(self):
        if self.body:
            return {
                'title': self.title,
                'content': self.body
            }
        elif self.source_file:
            try:
                content = self.source_file.read().decode('utf-8')
                return {
                    'title': self.title or self.source_file.name,
                    'content': content
                }
            except UnicodeDecodeError:
                return {
                    'title': self.title or self.source_file.name,
                    'content': "Unable to read file (not a text file)"
                }
        return {'title': self.title, 'content': ''}
        
    

