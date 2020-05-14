from django import forms

from .models import Post

from tinymce.widgets import TinyMCE

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'time_to_read',
            'moderator',
            'title',
            'description',
            'title_image',
            'publication',   
        ]


