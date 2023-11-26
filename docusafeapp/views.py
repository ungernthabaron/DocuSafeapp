from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect


from .models import Project, SafePassword, Documentation
from .forms import ProjectForm, DocumentationForm, LoginForm

def custom_logout(request):
    logout(request)
    return redirect('login')  # Replace 'login' with the actual name of your login URL

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def project_management(request):
    if request.user.is_authenticated:
        user_projects = Project.objects.filter(user=request.user)
        print(user_projects)  # Add this line for debugging
        return render(request, 'project_management.html', {'user_projects': user_projects})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_management')
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})

@login_required
def add_documentation(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = DocumentationForm(request.POST)
        if form.is_valid():
            documentation = form.save(commit=False)
            documentation.project = project
            documentation.save()
            return redirect('project_management')
    else:
        form = DocumentationForm()

    return render(request, 'add_documentation.html', {'form': form, 'project': project})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})