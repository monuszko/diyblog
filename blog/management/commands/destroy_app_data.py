from django.core.management.base import BaseCommand

from blog.models import Author, Bio, BlogPost, Comment


class Command(BaseCommand):
    help = """Destroys all data in the app tables.
            Used to clean up after 'create_sample_data'."""

    def handle(self, *args, **options):
        Author.objects.all().delete()
        Bio.objects.all().delete()
        BlogPost.objects.all().delete()
        Comment.objects.all().delete()
