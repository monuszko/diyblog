from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.BlogPostList.as_view(), name='blogpost_list'),
    path('<int:pk>/', views.BlogPostDetail.as_view(), name='post_detail'),
    path('blogger/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('bloggers/', views.AuthorList.as_view(), name='author_list'),
]
