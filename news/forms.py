from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Post, Author


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    class Meta:
       model = Post
       type = 'NW'
       fields = ['title',
                 'post_author',
                 'text',
                 'type',
                 'post_rating',
                 'category',
                 ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        text = cleaned_data.get("text")

        if name == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data
