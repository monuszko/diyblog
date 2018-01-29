from django.core.management.base import BaseCommand

from blog import factories
from blog.models import BlogPost, Author


class Command(BaseCommand):
    help = "Populates the database with sample data to illustrate the app."

    def handle(self, *args, **options):
        for x in range(9):
            a = factories.AuthorFactory()
            if a.pk < 7:
                factories.BioFactory(author=a)

        authors = Author.objects.all()
        bool(authors)
        num_posts = 37
        for y in range(num_posts):
            factories.BlogPostFactory(author=authors[y % authors.count()])

        posts = BlogPost.objects.all()
        bool(posts)
        num_comments = 241
        for y in range(num_comments):
            factories.CommentFactory(
                    author=authors[y % len(authors)],
                    blogpost=posts[y % len(posts)])


