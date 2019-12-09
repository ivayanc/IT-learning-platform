from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import SystemUser


class SystemUserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        self.model = SystemUser
        super(SystemUserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'login'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'pass',
        }
    ))

    class Meta():
        model = SystemUser
        fields = ('username', 'password')

class SystemUserCreationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name<br>')
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address<br>')
    about = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'About'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), help_text='Мінімум 8 символів<br>')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta(UserCreationForm.Meta):
        model = SystemUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'about', 'email',)

class SystemUserChangeForm(UserChangeForm):

    class Meta:
        model = SystemUser
        fields = ('email', 'name', 'about')
