from django.test import TestCase


from blog.models import Author, Bio, BlogPost, Comment
from blog import factories


class AuthorTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        factories.AuthorFactory()

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)

        self.assertEqual(author.get_absolute_url(), '/blog/blogger/1/')


class BioTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        factories.AuthorFactory()
        factories.BioFactory()

    def test_content_max_length(self):
        bio = Bio.objects.get(id=1)

        max_length = bio._meta.get_field('content').max_length
        self.assertEquals(max_length, 2000)

    def test_object_name(self):
        bio = Bio.objects.get(id=1)
        expected_name = bio.author.username
        self.assertEquals(expected_name, str(bio))
     

class BlogPostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        factories.AuthorFactory()
        factories.BlogPostFactory()

    def test_pub_date_label(self):
        bp = BlogPost.objects.get(id=1)
        label = bp._meta.get_field('pub_date').verbose_name
        self.assertEquals(label, 'publication date')

    def test_title_max_length(self):
        bp = BlogPost.objects.get(id=1)

        max_length = bp._meta.get_field('title').max_length
        self.assertEquals(max_length, 300)

    def test_content_max_length(self):
        bp = BlogPost.objects.get(id=1)

        max_length = bp._meta.get_field('content').max_length
        self.assertEquals(max_length, 5000)

    def test_object_name(self):
        bp = BlogPost.objects.get(id=1)
        expected_name = bp.title
        self.assertEquals(expected_name, str(bp))
     
    def test_get_absolute_url(self):
        bp = BlogPost.objects.get(id=1)

        self.assertEqual(bp.get_absolute_url(), '/blog/1/')


class CommentTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        factories.AuthorFactory()
        factories.BlogPostFactory()
        factories.CommentFactory()

    def test_pub_date_label(self):
        com = Comment.objects.get(id=1)
        label = com._meta.get_field('pub_date').verbose_name
        self.assertEquals(label, 'publication date')

    def test_content_max_length(self):
        com = Comment.objects.get(id=1)
        max_length = com._meta.get_field('content').max_length
        self.assertEquals(max_length, 1000)

    def test_object_name(self):
        com = Comment.objects.get(id=1)
        expected_name = "%s %s" % (com.blogpost, com.author)
        self.assertEquals(expected_name, str(com))
