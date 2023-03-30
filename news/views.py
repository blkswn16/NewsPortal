from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post, Author


class NewsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 20

class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
