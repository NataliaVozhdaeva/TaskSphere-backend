from django.contrib import admin
# Temporarily comment out admin registration to isolate the issue
# from .models import Task

# Register Task model
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ['title', 'status', 'assigned_to', 'created_at', 'updated_at']
#     list_filter = ['status', 'created_at', 'assigned_to']
#     search_fields = ['title', 'description']
#     readonly_fields = ['created_at', 'updated_at']
