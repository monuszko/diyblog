from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogPost, Author


class BlogPostList(ListView):
    model = BlogPost


class BlogPostDetail(DetailView):
    model = BlogPost


class AuthorList(ListView):
    model = Author
    template_name = 'blog/author_list.html'
    context_object_name = 'author_list'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'blog/author_detail.html'
