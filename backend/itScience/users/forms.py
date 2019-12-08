from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SystemUser

class SystemUserCreationForm(UserCreationForm):

    class Meta:
        model = SystemUser
        fields = ('username', 'email', 'name', 'about')

class SystemUserChangeForm(UserChangeForm):

    class Meta:
        model = SystemUser
        fields = ('username', 'email', 'name', 'about')

class SystemUserEditForm(forms.ModelForm):

    class Meta:
        model = SystemUser
        fields = [
            'email',
            'name',
            'about'
        ]