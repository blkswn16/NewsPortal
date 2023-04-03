from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,  PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class NewsList(ListView):
    model = Post
    ordering = '-time_created'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = 'news.add_post'

class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = 'news.change_post'


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    permission_required = 'news.delete_post'

class PostSearch(ListView):
    model = Post
    ordering = 'title'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesList(ListView):
    model = Post
    queryset = Post.objects.filter(type='article')
    ordering = '-time_date'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticleCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'
    permission_required = 'news.add_post'

class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'
    permission_required = 'news.change_post'

class ArticleDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')
    permission_required = 'news.delete_post'
