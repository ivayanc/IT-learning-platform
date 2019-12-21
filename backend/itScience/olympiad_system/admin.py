from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission

from .models import *
# Register your models here.

class TaskInline(admin.TabularInline):
    model = Task
    
class CriteriaInline(admin.TabularInline):
    model = Criteria
    

class ReviewInLine(admin.TabularInline):
    model = Review
    readonly_fields = ('criteria', )
    fields = ('criteria','result',)

@admin.register(Olympiad)
class OlympiadAdmin(admin.ModelAdmin):
    list_display = ('title', 'olymp_type', 'start_time', 'duration')
    model = Olympiad
    inlines = (TaskInline,)
    # fields = ('reviewers',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ('task_type','olympiad')
    list_display = ('title', 'task_type', 'olympiad')
    model = Task
    inlines = (CriteriaInline,)


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    
    list_display = ('encrypted_id', 'task', 'status', 'task')
    model = Solution
    inlines = (ReviewInLine,)
    list_filter = ('task','status')
    readonly_fields = ('encrypted_id', 'task', 'solution_file',)
    fields = ('encrypted_id', 'task', 'solution_file','status', 'reviewer')

  



admin.site.register(Criteria)