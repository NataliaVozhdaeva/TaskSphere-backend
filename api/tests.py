from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            assigned_to=self.user
        )

    def test_task_creation(self):
        """Test that a task can be created"""
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.assigned_to, self.user)
        self.assertEqual(self.task.status, 'to_do')

    def test_task_str_representation(self):
        """Test the string representation of a task"""
        self.assertEqual(str(self.task), 'Test Task')


class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_tasks(self):
        """Test getting tasks list"""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        """Test creating a new task"""
        data = {
            'title': 'New Task',
            'description': 'New Description'
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
