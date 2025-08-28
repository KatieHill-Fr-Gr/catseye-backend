from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    job_title = models.CharField(max_length=150, blank=True, default='')
    profile_img = models.URLField(max_length=255, blank=True, help_text="Cloudinary image URL")
    team = models.ForeignKey(to='teams.Team', on_delete=models.SET_NULL, null=True, blank=True)

