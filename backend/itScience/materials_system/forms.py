from django import forms

from .models import Post

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'category',
            'time_to_read',
            'moderator',
            'title',
            'views',
            'description',
            'title_image',
            'publication',   
        ]

