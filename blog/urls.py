from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.BlogPostList.as_view(), name='blogpost_list'),
    path('<int:pk>/', views.BlogPostDetail.as_view(), name='post_detail'),
    path('<int:pk>/comment', views.CommentCreate.as_view(), name='comment_create'),
    path('blogger/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('bloggers/', views.AuthorList.as_view(), name='author_list'),
]
