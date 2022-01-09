from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'user',
            'content',
            'image'
        ]

    def clean(self, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise forms.ValidationError("Content or Image required")
        return super().clean(**kwargs)
