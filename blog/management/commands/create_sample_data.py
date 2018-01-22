from django.core.management.base import BaseCommand

from blog import factories


class Command(BaseCommand):
    help = "Populates the database with sample data to illustrate the app."

    def handle(self, *args, **options):
        for x in range(9):
            factories.AuthorFactory()
        for y in range(6):
            factories.BioFactory()
        for y in range(37):
            factories.BlogPostFactory()
        for y in range(241):
            factories.CommentFactory()


