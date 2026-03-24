import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasksphere.settings')
django.setup()
from api.models import Task

print('Updating tasks with old status values...')
pending_count = Task.objects.filter(status='pending').count()
completed_count = Task.objects.filter(status='completed').count()

print(f'Found {pending_count} tasks with pending status')
print(f'Found {completed_count} tasks with completed status')

Task.objects.filter(status='pending').update(status='to_do')
Task.objects.filter(status='completed').update(status='ready')

print('Update complete!')
print('Current status counts:')
for status_choice, status_label in Task.STATUS_CHOICES:
    count = Task.objects.filter(status=status_choice).count()
    print(f'  {status_label}: {count}')
