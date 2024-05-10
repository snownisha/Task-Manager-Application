from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks),
    path('tasks/add/', views.add_tasks),
    path('tasks/<int:task_id>/', views.update_task),
    path('tasks/filter/<str:priority>/', views.filter_tasks_by_priority),
]