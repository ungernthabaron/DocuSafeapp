# DocuSafeApp/models.py
from django.db import models
from django.contrib.auth.models import User

class SafePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='default_title')
    password = models.CharField(max_length=255)
    description = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Documentation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
