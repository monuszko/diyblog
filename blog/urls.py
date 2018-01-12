from django.urls import path

from . import views


urlpatterns = [
    path('', views.BlogPostList.as_view(), name='index'),
    path('<int:pk>/', views.BlogPostDetail.as_view(), name='post'),
    path('blogger/<int:pk>/', views.AuthorDetail.as_view(), name='author'),
    path('bloggers/', views.AuthorList.as_view(), name='authors'),
]
