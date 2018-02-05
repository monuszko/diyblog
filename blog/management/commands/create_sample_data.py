from django.core.management.base import BaseCommand
from django.db import connection

from blog import factories
from blog.models import BlogPost, Author, Comment, Bio

class Command(BaseCommand):
    help = "Populates the database with sample data to illustrate the app."

    def handle(self, *args, **options):
        # Can't use bulk_create for these, because they need
        # to be assigned to 'Bloggers' group.
        authors = factories.AuthorFactory.create_batch(9)
        bios = [factories.BioFactory.build(author=au) for au in authors[:7]]
        Bio.objects.bulk_create(bios)

        num_posts = 37
        posts = [
                factories.BlogPostFactory.build(
                    author=authors[np % len(authors)]
                    )
                for np in range(num_posts)
                ]
        BlogPost.objects.bulk_create(posts)

        posts = BlogPost.objects.all()
        num_comments = 241
        comments = [
                factories.CommentFactory.build(
                    author=authors[y % len(authors)],
                    blogpost=posts[y % len(posts)]
                    )
                    for y in range(num_comments)
                ]

        Comment.objects.bulk_create(comments)
        print("Queries executed:", len(connection.queries))


