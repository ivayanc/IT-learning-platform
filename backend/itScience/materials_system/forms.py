from django import forms
from django.conf import settings
from .models import SystemUser

from .models import Post, HashTag

from ckeditor.widgets import CKEditorWidget

class PostCreateForm(forms.ModelForm):
    time_to_read = forms.CharField(label = "Прочитаєте за", max_length = 250)
    moderator = forms.ModelChoiceField(queryset = SystemUser.objects, label = "Автор")
    title = forms.CharField(label = "Заголовок", max_length = 255)
    description = forms.CharField(label = "Короткий опис", max_length = 150)
    title_image = forms.ImageField(label = "Головне зображення")
    publication = forms.CharField(label = "Текст публікації", widget=CKEditorWidget())
    
    class Meta:
        model = Post
        fields = (
            'time_to_read',
            'moderator',
            'title',
            'description',
            'title_image',
            'publication',   
        )

class HashTagForm(forms.ModelForm):
    class Meta:
        model = HashTag
        fields = [
            'tag_name',
            'tag_main',
        ]


