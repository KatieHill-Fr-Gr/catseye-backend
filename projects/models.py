from django.db import models
from django.contrib.postgres.fields import ArrayField

class Project(models.Model):
    
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('review', 'Under Review'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=255)
    brief = models.TextField(max_length=2000)
    deadline = models.DateField() 
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='in_progress') 

    images = ArrayField(models.URLField(max_length=500), size=4, default=list, blank=True, help_text='Upload max 4 image urls')

    team = models.ForeignKey(to='teams.Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='team_projects')
    owner = models.ForeignKey(to='users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='owned_projects')


    def __str__(self):
        return self.name

