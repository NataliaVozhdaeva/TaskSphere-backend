#!/usr/bin/env python3
"""
New User Workflow: Sign up, Login, and Create Tasks
"""
import requests
import json

# Base URL
BASE_URL = "http://localhost:8000/api"

def create_new_user_and_task():
    print("=== New User Workflow ===\n")
    
    # Step 1: Sign up as a new user
    print("1. Creating new user account...")
    username = "newuser_" + str(int(time.time()))  # Unique username
    register_data = {
        "username": username,
        "email": f"{username}@example.com", 
        "password": "mypassword123",
        "password_confirm": "mypassword123",
        "first_name": "New",
        "last_name": "User"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/register/", json=register_data)
        if response.status_code == 201:
            print("[SUCCESS] New user account created!")
            user_data = response.json()
            print(f"   Username: {user_data['user']['username']}")
            print(f"   Email: {user_data['user']['email']}")
            print(f"   User ID: {user_data['user']['id']}")
        else:
            print(f"[ERROR] Registration failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to server. Make sure the Django server is running on localhost:8000")
        return
    
    # Step 2: Login with new user credentials
    print(f"\n2. Logging in as {username}...")
    login_data = {
        "username": username,
        "password": "mypassword123"
    }
    
    response = requests.post(f"{BASE_URL}/login/", json=login_data)
    if response.status_code == 200:
        print("[SUCCESS] Login successful!")
        token_data = response.json()
        token = token_data['token']
        print(f"   Auth Token: {token[:20]}...")
    else:
        print(f"[ERROR] Login failed: {response.status_code}")
        print(f"   Response: {response.text}")
        return
    
    # Step 3: Create headers with authentication
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    # Step 4: Create your first task
    print("\n3. Creating your first task...")
    task_data = {
        "title": "Learn Django REST Framework",
        "description": "Complete the official Django REST Framework tutorial and build a sample API project"
    }
    
    response = requests.post(f"{BASE_URL}/tasks/", json=task_data, headers=headers)
    if response.status_code == 201:
        print("[SUCCESS] Task created successfully!")
        task = response.json()
        print(f"   Task ID: {task['id']}")
        print(f"   Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Status: {task['status']}")
        print(f"   Assigned to: {task['assigned_to']}")
    else:
        print(f"[ERROR] Task creation failed: {response.status_code}")
        print(f"   Response: {response.text}")
        return
    
    # Step 5: Create more tasks
    print("\n4. Creating more tasks...")
    
    tasks_to_create = [
        {
            "title": "Build a portfolio website",
            "description": "Create a personal portfolio website to showcase projects"
        },
        {
            "title": "Read Clean Code book",
            "description": "Read and take notes from 'Clean Code' by Robert C. Martin"
        },
        {
            "title": "Contribute to open source",
            "description": "Find an interesting open source project and make a contribution"
        }
    ]
    
    for i, task_info in enumerate(tasks_to_create, 1):
        response = requests.post(f"{BASE_URL}/tasks/", json=task_info, headers=headers)
        if response.status_code == 201:
            task = response.json()
            print(f"   [SUCCESS] Created task {i}: {task['title']}")
        else:
            print(f"   [ERROR] Failed to create task {i}: {response.status_code}")
    
    # Step 6: List all your tasks
    print("\n5. Listing all your tasks...")
    response = requests.get(f"{BASE_URL}/tasks/", headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        tasks = response_data['results']
        print(f"[SUCCESS] You have {len(tasks)} tasks:")
        for task in tasks:
            print(f"   - {task['id']}: {task['title']} ({task['status']})")
    else:
        print(f"[ERROR] Failed to list tasks: {response.status_code}")
    
    # Step 7: Update a task status
    print("\n6. Updating task status...")
    if tasks:
        first_task_id = tasks[0]['id']
        update_data = {"status": "in_progress"}
        response = requests.patch(f"{BASE_URL}/tasks/{first_task_id}/", json=update_data, headers=headers)
        if response.status_code == 200:
            updated_task = response.json()
            print(f"[SUCCESS] Updated task '{updated_task['title']}' status to '{updated_task['status']}'")
        else:
            print(f"[ERROR] Failed to update task: {response.status_code}")
    
    print(f"\n=== Workflow Complete ===")
    print(f"Your username: {username}")
    print(f"Your password: mypassword123")
    print(f"You can now login and manage your tasks!")

if __name__ == "__main__":
    import time
    create_new_user_and_task()
