from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import SystemUser

class SystemUserLoginForm(AuthenticationForm):

    username = forms.CharField(label="Логін", help_text="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'login'}))
    password = forms.CharField(label="Пароль", help_text="",  widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'pass',
        }
    ))

    class Meta():
        model = SystemUser
        fields = ('Логін', 'Пароль')

class SystemUserCreationForm(UserCreationForm):

    username = forms.CharField(label="Логін", help_text="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id' : 'login'}))
    first_name = forms.CharField(label="Ім'я", help_text="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "", 'id' : 'first_name'}), max_length=32)
    email=forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '', 'id' : 'email'}), max_length=64)
    about = forms.CharField(label="Інформація про себе", help_text="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id' : 'about'}), required = False)
    password1=forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '','id' : 'pass'}))
    password2=forms.CharField(label="Пароль ще раз", help_text="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '','id' : 'pass'}))

    class Meta(UserCreationForm.Meta):
        model = SystemUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'about', 'email',)

class SystemUserChangeForm(UserChangeForm):
    password2=forms.CharField(label="Новий пароль(якщо не хочете змінювати залишить порожнім)", required = False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '','id' : 'pass'}))
    class Meta:
        model = SystemUser
        fields = ('name', 'about', 'avatar', 'password')
