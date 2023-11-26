# docusafeapp/urls.py
from django.urls import path
from .views import add_project, register, project_management, custom_logout, add_documentation, project_detail
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('add_project/', add_project, name='add_project'),
    path('register/', register, name='register'),
    path('', project_management, name='project_management'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('add_documentation/<int:project_id>/', add_documentation, name='add_documentation'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),

]
