from django import forms

from .models import Update as UpdateModel


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModel
        fields = [
            "user",
            "content",
            "image"
        ]

    def clean(self, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        image = data.get("image", None)
        if content == "":
            content = None
        if content is None and image is None:
            raise forms.ValidationError('Content or Image required.')
        return super().clean(**kwargs)
