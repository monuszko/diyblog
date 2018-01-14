from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogPost, Author, Comment


def index(request):
    context = {}
    context['num_posts'] = BlogPost.objects.all().count()
    context['num_authors'] = Author.objects.all().count()
    context['num_comments'] = Comment.objects.all().count()
    return render(request, 'blog/index.html', context)


class BlogPostList(ListView):
    model = BlogPost
    paginate_by = 5


class BlogPostDetail(DetailView):
    model = BlogPost


class AuthorList(ListView):
    model = Author
    template_name = 'blog/author_list.html'
    context_object_name = 'author_list'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'blog/author_detail.html'
