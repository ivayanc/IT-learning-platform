from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission

from .models import *
# Register your models here.

class TaskInline(admin.TabularInline):
    model = Task
    
class CriteriaInline(admin.TabularInline):
    model = Criteria
    
class ReviewGroup(admin.TabularInline):
    model = Group

@admin.register(Olympiad)
class OlympiadAdmin(admin.ModelAdmin):
    list_display = ('title', 'olymp_type', 'start_time', 'duration')
    model = Olympiad
    inlines = (TaskInline,)
    # fields = ('reviewers',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task_type', 'olympiad')
    model = Task
    inlines = (CriteriaInline,)

admin.site.register(Solution)
admin.site.register(Criteria)