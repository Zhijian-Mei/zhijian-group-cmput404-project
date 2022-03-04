from django.test import TestCase
from .models import *
from django.utils import timezone
import uuid

class TestAuthor(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user",
            password="password123"
        )
        self.author = AuthorModel.objects.create(
            user = self.user,
            id = '553b1321-00d5-43f1-8f5c-a1fe6ed63297',
            host = "127.0.0.1",
            displayName = "somename",
            github='githuburls',
            profileImage='somesrc'
        )

    def testId(self):
        self.assertEquals(self.author.id, "553b1321-00d5-43f1-8f5c-a1fe6ed63297")

    def testHost(self):
        self.assertEquals(self.author.host, "127.0.0.1")

    def testDisplayName(self):
        self.assertEquals(self.author.displayName, "somename")

    def testGithub(self):
        self.assertEquals(self.author.github, "githuburls")

    def testProfileImage(self):
        self.assertEquals(self.author.profileImage, "somesrc")

class TestPost(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user",
            password="password123"
        )
        self.author = AuthorModel.objects.create(
            user = self.user,
            id = '553b1321-00d5-43f1-8f5c-a1fe6ed63297',
            host = "127.0.0.1",
            displayName = "somename",
            github='githuburls',
            profileImage='somesrc'
        )
        self.post = PostModel.objects.create(
            title = 'posttitle',
            id = '553b1321-00d5-43f1-8f5c-a1fe6ed63298',
            source = 'sourceaddress/uuid',
            origin = 'originaddress/uuid',
            description = 'descriptions',
            contentType = 'contenttype',
            content = 'content',
            author = self.author,
            categories = 'ctg',
            count = 123,
            comments = 'comments',
            visibility = 'PUBLIC',
            unlisted = 'True'
        )

    def testTitle(self):
        self.assertEquals(self.post.title, "posttitle")

    def testId(self):
        self.assertEquals(self.post.id, "553b1321-00d5-43f1-8f5c-a1fe6ed63298")

    def testSource(self):
        self.assertEquals(self.post.source, "sourceaddress/uuid")

    def testOrigin(self):
        self.assertEquals(self.post.origin, "originaddress/uuid")

    def testDescription(self):
        self.assertEquals(self.post.description, "descriptions")

    def testContentType(self):
        self.assertEquals(self.post.contentType, "contenttype")

    def testContent(self):
        self.assertEquals(self.post.content, "content")

    def testCategories(self):
        self.assertEquals(self.post.categories, "ctg")

    def testCount(self):
        self.assertEquals(self.post.count, 123)

    def testComments(self):
        self.assertEquals(self.post.comments, "comments")

    def testVisibility(self):
        self.assertEquals(self.post.visibility, "PUBLIC")

    def testUnlisted(self):
        self.assertEquals(self.post.unlisted, "True")
