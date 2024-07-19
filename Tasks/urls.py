from django.urls import path
from .views import create_task_view, show_all_tasks_view, delete_task_view

urlpatterns = [
    path('create-task/', create_task_view, name='create-task'),
    path('show-all-tasks/', show_all_tasks_view, name='show-tasks'),
    path('delete/<task_id>/', delete_task_view, name='delete-task'),
]