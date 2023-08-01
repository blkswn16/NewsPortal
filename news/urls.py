from django.urls import path
from .views import NewsList, NewsDetail, PostCreate, PostUpdate, PostDelete, PostSearch, CategoryList, subscribe, unsubscribe

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
   path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe')
]
