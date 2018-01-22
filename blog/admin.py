from django.contrib import admin

from .models import BlogPost, Comment, Author, Bio



class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('pub_date',)
    extra = 1

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [
            CommentInline,
            ]


class BioInline(admin.TabularInline):
    model = Bio

class BlogPostInline(admin.TabularInline):
    model = BlogPost
    readonly_fields = ('pub_date',)
    show_change_link = True
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'username', 'password', 'email', 'is_active')
    inlines = [
            BioInline,
            BlogPostInline,
            ]
