from . import views
from django.urls import path
from .views import (
    HomePage,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    # Home page, redirects to task list if user is authenticated
    path('', views.HomePage.as_view(), name='home'),

    # Task list view
    path('tasks/', views.TaskListView.as_view(), name='task_list'),

    # Create new task
    path('task/new/', views.TaskCreateView.as_view(), name='task_new'),

    # View task details
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),

    # Edit a task
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),  # Corrected to TaskUpdateView

    # Delete a task
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]