import factory

from faker import Faker

from .models import Author, Bio, BlogPost, Comment



fake = Faker()


class BioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bio

    author = factory.Iterator(Author.objects.all())
    content = '\n\n'.join(fake.paragraphs(nb=4))[:2000]


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Sequence(lambda n: "First name %03d" % n)
    last_name = factory.Sequence(lambda n: "Last name %03d" % n)
    username = factory.Sequence(lambda n: "author%03d" % n)
