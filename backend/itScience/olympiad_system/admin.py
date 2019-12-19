from django.contrib import admin

from .models import *
# Register your models here.

class TaskInline(admin.TabularInline):
    model = Task
    
class CriteriaInline(admin.TabularInline):
    model = Criteria
    

@admin.register(Olympiad)
class OlympiadAdmin(admin.ModelAdmin):
    list_display = ('title', 'olymp_type', 'start_time', 'duration')
    model = Olympiad
    inlines = (TaskInline,)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task_type', 'olympiad')
    model = Task
    inlines = (CriteriaInline,)