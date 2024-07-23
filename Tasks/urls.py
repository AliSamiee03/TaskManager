from django.urls import path
from .views import create_task_view, show_all_tasks_view, delete_task_view, update_task_view, show_categories, create_category_view

urlpatterns = [
    path('create-task/', create_task_view, name='create-task'),
    path('show-all-tasks/', show_all_tasks_view, name='show-tasks'),
    path('delete/<task_id>/', delete_task_view, name='delete-task'),
    path('update/<task_id>/', update_task_view, name='update-task'),
    path('show-categories/', show_categories, name='categories'),
    path('create-category/', create_category_view, name='create-category'),
]