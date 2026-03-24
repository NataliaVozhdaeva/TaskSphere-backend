import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasksphere.settings')
django.setup()
from api.models import Task

print('Updating tasks with "ready" status to "completed"...')
ready_count = Task.objects.filter(status='ready').count()

print(f'Found {ready_count} tasks with "ready" status')

Task.objects.filter(status='ready').update(status='completed')

print('Update complete!')
print('Current status counts:')
for status_choice, status_label in Task.STATUS_CHOICES:
    count = Task.objects.filter(status=status_choice).count()
    print(f'  {status_label}: {count}')
