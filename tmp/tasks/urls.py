from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks, name="get tasks"),
    path('tasks/add/', views.add_tasks, name="view tasks"),
    path('tasks/<int:task_id>/', views.update_task, name="update tasks"),
    path('tasks/filter/<str:priority>/', views.filter_tasks_by_priority),
]