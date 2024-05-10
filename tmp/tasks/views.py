from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task
import json

# Create your views here.
def get_tasks(request):
    tasks = list(Task.objects.all().values())
    return JsonResponse(tasks, safe=False)

def add_tasks(request):
    if request.method =='POST':
        data = json.loads(request.body)
        task = Task.objects.create(**data)
        return JsonResponse({'message': 'Task added successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'}, status=405)

def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'PUT':
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.priority = data.get('priority', task.priority)
        task.status = data.get('status', task.status)
        task.save()
        return JsonResponse({'message': 'Task updated successfully'})

    return render(request, 'update_task.html', {'task': task})
    
def delete_tasks(request):
    pass

def filter_tasks_by_priority(request, priority):
    if request.method == 'GET':
        tasks = Task.objects.filter(priority=priority)
        tasks_data = list(tasks.values())
        return JsonResponse (tasks_data, safe=False)