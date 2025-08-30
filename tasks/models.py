from django.db import models


class Task(models.Model):

    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('review', 'Under Review'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    deadline = models.DateField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='in_progress')

    parent_project = models.ForeignKey(to='projects.Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='project_tasks')
    assigned_to = models.ForeignKey(to='users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    source_text = models.ForeignKey(to='source_texts.Source', on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    translation = models.ForeignKey(to='translations.Translation', on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')

