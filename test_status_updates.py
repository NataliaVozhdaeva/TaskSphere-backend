#!/usr/bin/env python3
"""
Test Task Status Update Functionality
"""
import requests
import json

# Base URL
BASE_URL = "http://localhost:8000/api"

def test_status_updates():
    print("=== Task Status Update Test ===\n")
    
    # Step 1: Login as existing user
    print("1. Logging in...")
    login_data = {
        "username": "myuser",
        "password": "mypassword123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/login/", json=login_data)
        if response.status_code == 200:
            print("[SUCCESS] Login successful!")
            token_data = response.json()
            token = token_data['token']
            print(f"   Token: {token[:20]}...")
        else:
            print(f"[ERROR] Login failed: {response.status_code}")
            return
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to server")
        return
    
    # Step 2: Create headers
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    # Step 3: Create a new task
    print("\n2. Creating a new task...")
    task_data = {
        "title": "Test Status Updates",
        "description": "This task will be used to test status updates"
    }
    
    response = requests.post(f"{BASE_URL}/tasks/", json=task_data, headers=headers)
    if response.status_code == 201:
        task = response.json()
        task_id = task['id']
        print(f"[SUCCESS] Task created with ID: {task_id}")
        print(f"   Initial status: {task['status']}")
    else:
        print(f"[ERROR] Failed to create task: {response.status_code}")
        return
    
    # Step 4: Test status updates
    print("\n3. Testing status updates...")
    
    status_updates = [
        ("in_progress", "In Progress"),
        ("ready", "Ready"),
        ("outdated", "Outdated"),
        ("to_do", "To Do")
    ]
    
    for status_value, status_label in status_updates:
        print(f"\n   Updating to {status_label}...")
        update_data = {"status": status_value}
        
        response = requests.patch(f"{BASE_URL}/tasks/{task_id}/", json=update_data, headers=headers)
        if response.status_code == 200:
            updated_task = response.json()
            print(f"   [SUCCESS] Status updated to: {updated_task['status']}")
        else:
            print(f"   [ERROR] Failed to update status: {response.status_code}")
            print(f"   Response: {response.text}")
    
    # Step 5: Test invalid status
    print(f"\n4. Testing invalid status update...")
    update_data = {"status": "invalid_status"}
    
    response = requests.patch(f"{BASE_URL}/tasks/{task_id}/", json=update_data, headers=headers)
    if response.status_code == 400:
        print("[SUCCESS] Invalid status correctly rejected")
        print(f"   Error: {response.json()}")
    else:
        print(f"[ERROR] Expected validation error but got: {response.status_code}")
    
    # Step 6: List all tasks with current status
    print(f"\n5. Listing all tasks with current status...")
    response = requests.get(f"{BASE_URL}/tasks/", headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        tasks = response_data['results']
        print(f"[SUCCESS] Found {len(tasks)} tasks:")
        for task in tasks:
            print(f"   - {task['id']}: {task['title']} ({task['status']})")
    else:
        print(f"[ERROR] Failed to list tasks: {response.status_code}")
    
    print("\n=== Status Update Test Complete ===")
    print("Available statuses:")
    print("  - to_do (default)")
    print("  - in_progress") 
    print("  - ready")
    print("  - outdated")

if __name__ == "__main__":
    test_status_updates()
