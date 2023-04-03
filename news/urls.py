from django.urls import path
from .views import NewsList, NewsDetail, PostCreate, PostUpdate, PostDelete, PostSearch, ArticlesList, ArticleDelete, ArticleCreate, ArticleUpdate

urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('news/', NewsList.as_view(), name='news_list'),
   path('news/create', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit', PostUpdate.as_view(), name='post_edit'),
   path('news/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/', ArticlesList.as_view(), name='articles_list'),
   path('articles/create', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/edit', ArticleUpdate.as_view(), name='article_edit'),
   path('articles/<int:pk>/delete', ArticleDelete.as_view(), name='post_delete'),
]
