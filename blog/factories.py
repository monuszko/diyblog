import pytz
import factory
from faker import Faker

from django.conf import settings
from django.utils.timezone import now

from .models import Author, Bio, BlogPost, Comment

TIMEZONE = pytz.timezone(settings.TIME_ZONE)
TODAY = now()

fake = Faker()


# Caution: don't make more than Authors, because it's OneToOneField
class BioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bio

    author = factory.Iterator(Author.objects.all())
    content = factory.LazyFunction(lambda: '\n\n'.join(fake.paragraphs(nb=4))[:2000])


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Sequence(lambda n: "First name %03d" % n)
    last_name = factory.Sequence(lambda n: "Last name %03d" % n)
    username = factory.Sequence(lambda n: "author%03d" % n)


class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = factory.LazyFunction(
            lambda: fake.sentence(nb_words=6, variable_nb_words=True)[:200])
    content = factory.LazyFunction(
            lambda: '\n\n'.join(fake.paragraphs(nb=14))[:5000])
    author = factory.Iterator(Author.objects.all())
    pub_date = factory.LazyFunction(
            lambda: fake.past_datetime(start_date="-30d", tzinfo=TIMEZONE))


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    blogpost = factory.Iterator(BlogPost.objects.all())
    content = factory.LazyFunction(
            lambda: '\n\n'.join(fake.paragraphs(nb=3))[:2000])
    author = factory.Iterator(Author.objects.all())

    # Comments must not be older than the article... but not in the future
    @factory.lazy_attribute
    def pub_date(self):
        blogpost_date = self.blogpost.pub_date
        return fake.date_time_between_dates(blogpost_date, TODAY, TIMEZONE)
