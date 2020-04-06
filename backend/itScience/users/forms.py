from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import SystemUser


class SystemUserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        self.model = SystemUser
        super(SystemUserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label="", help_text="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Логін', 'id': 'login'}))
    password = forms.CharField(label="", help_text="",  widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
            'id': 'pass',
        }
    ))

    class Meta():
        model = SystemUser
        fields = ('username', 'password')

class SystemUserCreationForm(UserCreationForm):

    username = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логін', 'id' : 'login'}))
    first_name = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я", 'id' : 'first_name'}), max_length=32)
    email=forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id' : 'email'}), max_length=64)
    about = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Інформація про себе', 'id' : 'about'}))
    password1=forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль','id' : 'pass'}))
    password2=forms.CharField(label="", help_text="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль ще раз','id' : 'pass'}))

    class Meta(UserCreationForm.Meta):
        model = SystemUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'about', 'email',)

class SystemUserChangeForm(UserChangeForm):

    class Meta:
        model = SystemUser
        fields = ('email', 'name', 'about')
