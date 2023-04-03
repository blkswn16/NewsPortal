from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter
from django import forms
from .models import Post, Author

class PostFilter(FilterSet):

    search_title = CharFilter(
        field_name='title',
        label='Заголовок',
        lookup_expr='icontains',
    )

    search_author = ModelChoiceFilter(
        empty_label='Все авторы',
        field_name='post_author',
        label='Автор',
        queryset=Author.objects.all(),
    )

    post_date__gt = DateFilter(
        field_name='time_created',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte',
    )

    class Meta:
        model = Post
        fields = ['type']

