from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
     author=models.OneToOneField(User, on_delete=models.CASCADE)
     rating = models.IntegerField(default=0)

     def update_rating(self):
         author_post_rating = self.post_set.all().aggregate(post_rating=Sum("post_rating"))['post_rating']
         author_comments_rating = self.author.comment_set.all().aggregate(comment_rating=Sum('comment_rating'))[
             'comment_rating']
         author_post_comments_rating = Comment.objects.filter(post__post_author=self.id).aggregate(comment_rating=Sum('comment_rating'))['comment_rating']
         self.rating = author_post_rating * 3 + author_comments_rating + author_post_comments_rating
         self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=255,
                                     unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories', blank=True)

    def __str__(self):
        return self.category_name


class Post(models.Model):

    article = 'AR'
    news = 'NE'
    TYPES = [(article, 'Статья'),
             (news, 'Новость')
             ]
    title = models.CharField(max_length=255)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=2,
                            choices=TYPES,
                            default=news)
    post_rating = models.FloatField(default=0.0)
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating += 1
        self.save()

    def preview(self):
        return self.text[0:124] + '...'

    def __str__(self):
        return f'{self.title}: {self.text[:20]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}, {self.post}'


class Comment(models.Model):
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    comment_rating = models.FloatField(default=0.0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
