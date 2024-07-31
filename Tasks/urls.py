from django.urls import path
from . import views

urlpatterns = [
    path('create-task/', views.create_task_view, name='create-task'),
    path('show-all-tasks/', views.show_all_tasks_view, name='show-tasks'),
    path('delete/<task_id>/', views.delete_task_view, name='delete-task'),
    path('update/<task_id>/', views.update_task_view, name='update-task'),
    path('show-categories/', views.show_categories, name='categories'),
    path('create-category/', views.create_category_view, name='create-category'),
    path('delete-category/<category_id>/', views.delete_category_view, name='delete-category'),
    path('update-category/<category_id>/', views.update_category_view, name='update-category'),
    path('show-tasks-by-category/<category_id>/', views.show_task_by_category_view, name='task-by-category'),
    path('comments/<task_id>/', views.comments_view, name='comments'),
    path('delete-comment/<task_id>/<comment_id>/', views.delete_comment_view, name='delete-comment'),
    path('public-tasks/', views.show_public_tasks_view, name='public-tasks'),
    path('search/', views.search_view, name='search')
]