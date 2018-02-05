from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from blog import factories
from blog.models import BlogPost, Comment, Author, Bio


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        blogposts = []
        for anum in range(13):
            au = factories.AuthorFactory()
            by_author = factories.BlogPostFactory.build_batch(19, author=au)
            blogposts.extend(by_author)
        BlogPost.objects.bulk_create(blogposts)

        authors = Author.objects.all()
        bios = [factories.BioFactory.build(author=au) for au in authors]
        Bio.objects.bulk_create(bios)

        comments = []
        for u in User.objects.all():
            for bp in BlogPost.objects.all():
                c = factories.CommentFactory.build(author=u, blogpost=bp)
                comments.append(c)
        Comment.objects.bulk_create(comments)

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
        blogposts = []
        bios = []
        for anum in range(13):
            a = factories.AuthorFactory()
            bios.append(factories.BioFactory.build(author=a))
            by_author = factories.BlogPostFactory.build_batch(19, author=a)
            blogposts.extend(by_author)

        Bio.objects.bulk_create(bios)
        BlogPost.objects.bulk_create(blogposts)


    def test_view_exists_at_desired_location(self):
        resp = self.client.get('/blog/posts/')
        self.assertEqual(resp.status_code, 200)


    def test_view_accessible_by_name(self):
        resp = self.client.get(reverse('blog:blogpost_list'))
        self.assertEqual(resp.status_code, 200)


class BlogPostDetailTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        bios = []
        blogposts = []
        for anum in range(13):
            a = factories.AuthorFactory()
            bios.append(factories.BioFactory.build(author=a))

            by_author = factories.BlogPostFactory.build_batch(19, author=a)
            blogposts.extend(by_author)
        Bio.objects.bulk_create(bios)
        BlogPost.objects.bulk_create(blogposts)

        comments = []
        for u in User.objects.all():
            for bp in BlogPost.objects.all():
                com = factories.CommentFactory.build(author=u, blogpost=bp)
                comments.append(com)
        Comment.objects.bulk_create(comments)

    def test_view_exists_at_desired_location(self):
        resp = self.client.get('/blog/3/')
        self.assertEqual(resp.status_code, 200)

    def test_view_accessible_by_name(self):
        resp = self.client.get(reverse('blog:post_detail', args=[3]))
        self.assertEqual(resp.status_code, 200)


class AuthorListTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        bios = []
        for anum in range(13):
            a = factories.AuthorFactory()
            bios.append(factories.BioFactory.build(author=a))
        Bio.objects.bulk_create(bios)

    def test_view_exists_at_desired_location(self):
        resp = self.client.get('/blog/bloggers/')
        self.assertEqual(resp.status_code, 200)

    def test_view_accessible_by_name(self):
        resp = self.client.get(reverse('blog:author_list'))
        self.assertEqual(resp.status_code, 200)


class AuthorDetailTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        bios = []
        blogposts = []
        for anum in range(13):
            a = factories.AuthorFactory()
            bios.append(factories.BioFactory.build(author=a))
            by_author = factories.BlogPostFactory.build_batch(19, author=a)
            blogposts.extend(by_author)
        Bio.objects.bulk_create(bios)
        BlogPost.objects.bulk_create(blogposts)

    def test_view_exists_at_desired_location(self):
        resp = self.client.get('/blog/blogger/4/')
        self.assertEqual(resp.status_code, 200)

    def test_view_accessible_by_name(self):
        resp = self.client.get(reverse('blog:author_detail', args=[4]))
        self.assertEqual(resp.status_code, 200)
