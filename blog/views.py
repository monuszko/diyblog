from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogPost, Author


class BlogPostList(ListView):
    model = BlogPost


class BlogPostDetail(DetailView):
    model = BlogPost


class AuthorList(ListView):
    model = Author


class AuthorDetail(DetailView):
    model = Author
