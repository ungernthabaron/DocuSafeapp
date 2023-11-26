# DocuSafeApp/admin.py
from django.contrib import admin
from .models import Project, Documentation

admin.site.register(Project)
admin.site.register(Documentation)
