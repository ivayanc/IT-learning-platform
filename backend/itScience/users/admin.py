from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import SystemUserCreationForm, SystemUserChangeForm
from .models import SystemUser, Role

class SystemUserAdmin(UserAdmin):
    add_form = SystemUserCreationForm
    form = SystemUserChangeForm
    model = SystemUser
    list_display = ['email', 'username', 'name', 'about']

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('name','about', 'avatar')}),
    )

@admin.register(Role)
class Role(admin.ModelAdmin):
    fields = (
    'role_name',
    'can_post',
    'can_edit_posts',
    'can_change_hashtags',
    'can_edit_users')
    list_display = ('role_name', 'can_post', 'can_edit_posts', 'can_change_hashtags', 'can_edit_users')
    filter_list = ('role_name')

admin.site.register(SystemUser, SystemUserAdmin)
