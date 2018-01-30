from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from blog import factories
from blog.models import BlogPost


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        for anum in range(13):
            a = factories.AuthorFactory()
            factories.BioFactory(author=a)
            for bpnum in range(19):
                bp = factories.BlogPostFactory(author=a)

        for u in User.objects.all():
            for bp in BlogPost.objects.all():
                factories.CommentFactory(author=u, blogpost=bp)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/bloggers/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blog:index'))
        self.assertEqual(resp.status_code, 200)

    def test_counts_authors(self):
        resp = self.client.get(reverse('blog:index'))
        self.assertTrue(resp.context['num_authors'] == 13)
        self.assertTrue(resp.context['num_posts'] == 13 * 19)
        self.assertEquals(resp.context['num_comments'], 13 * 19 * 13)


class BlogPostListTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        for anum in range(13):
            a = factories.AuthorFactory()
            factories.BioFactory(author=a)
            for bpnum in range(19):
                bp = factories.BlogPostFactory(author=a)

    def test_view_exists_at_desired_location(self):
        resp = self.client.get('/blog/posts/')
        self.assertEqual(resp.status_code, 200)


    def test_view_accessible_by_name(self):
        resp = self.client.get(reverse('blog:blogpost_list'))
        self.assertEqual(resp.status_code, 200)


class BlogPostDetailTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        for anum in range(13):
            a = factories.AuthorFactory()
            factories.BioFactory(author=a)
            for bpnum in range(19):
                bp = factories.BlogPostFactory(author=a)

        for u in User.objects.all():
            for bp in BlogPost.objects.all():
                factories.CommentFactory(author=u, blogpost=bp)

    def test_view_exists_at_desired_location(self):
        resp = self.client.get('/blog/3/')
        self.assertEqual(resp.status_code, 200)

    def test_view_accessible_by_name(self):
        resp = self.client.get(reverse('blog:post_detail', args=[3]))
        self.assertEqual(resp.status_code, 200)


class AuthorListTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        for anum in range(13):
            a = factories.AuthorFactory()
            factories.BioFactory(author=a)

    def test_view_exists_at_desired_location(self):
        resp = self.client.get('/blog/bloggers/')
        self.assertEqual(resp.status_code, 200)

    def test_view_accessible_by_name(self):
        resp = self.client.get(reverse('blog:author_list'))
        self.assertEqual(resp.status_code, 200)


class AuthorDetailTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        for anum in range(13):
            a = factories.AuthorFactory()
            factories.BioFactory(author=a)
            for bpnum in range(19):
                bp = factories.BlogPostFactory(author=a)

    def test_view_exists_at_desired_location(self):
        resp = self.client.get('/blog/blogger/4/')
        self.assertEqual(resp.status_code, 200)

    def test_view_accessible_by_name(self):
        resp = self.client.get(reverse('blog:author_detail', args=[4]))
        self.assertEqual(resp.status_code, 200)