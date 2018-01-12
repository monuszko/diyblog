from django.contrib import admin

from .models import BlogPost, Comment, Author, AuthorBio



class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('pub_date',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [
            CommentInline,
            ]


class AuthorBioInline(admin.TabularInline):
    model = AuthorBio

class BlogPostInline(admin.TabularInline):
    model = BlogPost
    readonly_fields = ('pub_date',)
    show_change_link = True

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [
            AuthorBioInline,
            BlogPostInline,
            ]
