from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

    def clean_data(self):
        data = self.cleaned_data["text"]
        if data == '':
            raise forms.ValidationError('Должен быть текст')

        return data
