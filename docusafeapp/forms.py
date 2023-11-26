# docusafeapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Documentation

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

class DocumentationForm(forms.ModelForm):
    class Meta:
        model = Documentation
        fields = ['title', 'content']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
