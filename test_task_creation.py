#!/usr/bin/env python3
"""
Test script for TaskSphere API - Task Creation
"""
import requests
import json

# Base URL
BASE_URL = "http://localhost:8000/api"

def test_task_creation():
    print("=== TaskSphere API Test ===\n")
    
    # Step 1: Register a test user (or use existing)
    print("1. Registering test user...")
    register_data = {
        "username": "testuser",
        "email": "test@example.com", 
        "password": "password123",
        "password_confirm": "password123",
        "first_name": "Test",
        "last_name": "User"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/register/", json=register_data)
        if response.status_code == 201:
            print("[SUCCESS] User registered successfully")
            user_data = response.json()
            print(f"   User ID: {user_data['user']['id']}")
        elif response.status_code == 400 and "username already exists" in response.text:
            print("[INFO] User already exists, proceeding with login")
        else:
            print(f"[ERROR] Registration failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to server. Make sure the Django server is running on localhost:8000")
        return
    
    # Step 2: Login to get token
    print("\n2. Logging in...")
    login_data = {
        "username": "admin",
        "password": "admin123"
    }
    
    response = requests.post(f"{BASE_URL}/login/", json=login_data)
    if response.status_code == 200:
        print("[SUCCESS] Login successful")
        token_data = response.json()
        token = token_data['token']
        print(f"   Token: {token[:20]}...")
    else:
        print(f"[ERROR] Login failed: {response.status_code}")
        print(f"   Response: {response.text}")
        return
    
    # Step 3: Create headers with authentication
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    # Step 4: Test task creation
    print("\n3. Creating tasks...")
    
    # Test 1: Valid task with title and description
    task_data = {
        "title": "Complete project documentation",
        "description": "Write comprehensive documentation for the TaskSphere API including endpoints and examples"
    }
    
    response = requests.post(f"{BASE_URL}/tasks/", json=task_data, headers=headers)
    if response.status_code == 201:
        print("[SUCCESS] Task created successfully (with title and description)")
        task = response.json()
        print(f"   Task ID: {task['id']}")
        print(f"   Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Status: {task['status']}")
    else:
        print(f"[ERROR] Task creation failed: {response.status_code}")
        print(f"   Response: {response.text}")
    
    # Test 2: Task with only title (description optional)
    task_data2 = {
        "title": "Review code changes"
    }
    
    response = requests.post(f"{BASE_URL}/tasks/", json=task_data2, headers=headers)
    if response.status_code == 201:
        print("[SUCCESS] Task created successfully (title only)")
        task = response.json()
        print(f"   Task ID: {task['id']}")
        print(f"   Title: {task['title']}")
        print(f"   Description: {task['description'] or '(empty)'}")
    else:
        print(f"[ERROR] Task creation failed: {response.status_code}")
        print(f"   Response: {response.text}")
    
    # Test 3: Invalid task (empty title)
    task_data3 = {
        "title": "",
        "description": "This should fail due to empty title"
    }
    
    response = requests.post(f"{BASE_URL}/tasks/", json=task_data3, headers=headers)
    if response.status_code == 400:
        print("[SUCCESS] Validation correctly rejected empty title")
        print(f"   Error: {response.json()}")
    else:
        print(f"[ERROR] Expected validation error but got: {response.status_code}")
    
    # Test 4: Invalid task (no title)
    task_data4 = {
        "description": "This should fail due to missing title"
    }
    
    response = requests.post(f"{BASE_URL}/tasks/", json=task_data4, headers=headers)
    if response.status_code == 400:
        print("[SUCCESS] Validation correctly rejected missing title")
        print(f"   Error: {response.json()}")
    else:
        print(f"[ERROR] Expected validation error but got: {response.status_code}")
    
    # Step 5: List all tasks for the user
    print("\n4. Listing all tasks...")
    response = requests.get(f"{BASE_URL}/tasks/", headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        tasks = response_data['results']
        print(f"[SUCCESS] Found {len(tasks)} tasks:")
        for task in tasks:
            print(f"   - {task['id']}: {task['title']} ({task['status']})")
    else:
        print(f"[ERROR] Failed to list tasks: {response.status_code}")
        print(f"   Response: {response.text}")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    test_task_creation()
