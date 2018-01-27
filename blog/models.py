from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.urls import reverse


class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(groups__name='Bloggers')

class Author(User):
    objects = AuthorManager()

    def get_absolute_url(self):
        return reverse("blog:author_detail", args=[self.pk])

    class Meta:
        proxy = True


class Bio(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.author.username


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(
            default=timezone.now,
            editable=False,
            verbose_name="publication date")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.pk])

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(
            default=timezone.now,
            editable=False,
            verbose_name="publication date")

    def __str__(self):
        return "{0} {1}".format(self.blogpost, self.author)

    class Meta:
        ordering = ['pub_date']

