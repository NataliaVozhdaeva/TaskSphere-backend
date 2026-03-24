import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasksphere.settings')
django.setup()
from api.models import Task

print('Tasks currently IN PROGRESS:')
in_progress_tasks = Task.objects.filter(status='in_progress')
for task in in_progress_tasks:
    print(f'  ID: {task.id}')
    print(f'  Title: {task.title}')
    print(f'  Assigned to: {task.assigned_to.username if task.assigned_to else "None"}')
    print(f'  Created: {task.created_at}')
    print('---')

print('\nHow to move tasks between statuses:')
print('1. to_do -> in_progress (when you start working)')
print('2. in_progress -> ready (when you finish)')
print('3. any -> outdated (when no longer relevant)')
