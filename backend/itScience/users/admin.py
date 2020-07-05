from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import SystemUserCreationForm, SystemUserChangeForm
from .models import SystemUser

class SystemUserAdmin(UserAdmin):
    add_form = SystemUserCreationForm
    form = SystemUserChangeForm
    model = SystemUser
    list_display = ['email', 'username', 'name', 'about']

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('name','about', 'avatar')}),
    )

admin.site.register(SystemUser, SystemUserAdmin)