from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

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


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('content',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blogpost = BlogPost.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # not reusing get_success_url because it might change in the future
        context['blog_link'] = reverse("blog:post_detail", args=[self.kwargs['pk']])
        return context
