from django.test import TestCase
from .models import *
from django.utils import timezone
import uuid
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
import json
from .models import PostModel


class TestAuthor(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user",
            password="password123"
        )
        self.author = AuthorModel.objects.create(
            user=self.user,
            id='553b1321-00d5-43f1-8f5c-a1fe6ed63297',
            host="127.0.0.1",
            displayName="somename",
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
            user=self.user,
            id='553b1321-00d5-43f1-8f5c-a1fe6ed63297',
            host="127.0.0.1",
            displayName="somename",
            github='githuburls',
            profileImage='somesrc'
        )
        self.post = PostModel.objects.create(
            title='posttitle',
            id='553b1321-00d5-43f1-8f5c-a1fe6ed63298',
            source='sourceaddress/uuid',
            origin='originaddress/uuid',
            description='descriptions',
            contentType='contenttype',
            content='content',
            image_src='image_src',
            image='image',
            author=self.author,
            author_object=self.author,
            categories='ctg',
            visibility='PUBLIC',
            unlisted='True'
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

    def testVisibility(self):
        self.assertEquals(self.post.visibility, "PUBLIC")

    def testUnlisted(self):
        self.assertEquals(self.post.unlisted, "True")

    def ImageTest(self):
        self.assertEquals(self.post.image, 'image')

    def ImageSrcTest(self):
        self.assertEquals(self.post.image_src, 'image_src')


class TestComment(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user",
            password="password123"
        )
        self.author = AuthorModel.objects.create(
            user=self.user,
            id='553b1321-00d5-43f1-8f5c-a1fe6ed63297',
            host="127.0.0.1",
            displayName="somename",
            github='githuburls',
            profileImage='somesrc'
        )

        self.post = PostModel.objects.create(
            title='posttitle',
            id='553b1321-00d5-43f1-8f5c-a1fe6ed63298',
            source='sourceaddress/uuid',
            origin='originaddress/uuid',
            description='descriptions',
            contentType='contenttype',
            content='content',
            image_src='image_src',
            image='image',
            author=self.author,
            author_object=self.author,
            categories='ctg',
            visibility='PUBLIC',
            unlisted='True'
        )

        self.comment = CommentModel.objects.create(

            id='98b9f7f7-ee3a-457e-aea4-375e88bb96b7',
            author=self.author,
            post=self.post,
            comment='adadada',
            contentType='sometype',
            published='03/04/2022 22:13:48'

        )

    def testId(self):
        self.assertEquals(self.comment.id, '98b9f7f7-ee3a-457e-aea4-375e88bb96b7')

    def testComment(self):
        self.assertEquals(self.comment.comment, 'adadada')

    def testContentype(self):
        self.assertEquals(self.comment.contentType, 'sometype')

    def testPublished(self):
        self.assertEquals(self.comment.published, '03/04/2022 22:13:48')


class TestLike(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user",
            password="password123"
        )
        self.author = AuthorModel.objects.create(
            user=self.user,
            id='553b1321-00d5-43f1-8f5c-a1fe6ed63297',
            host="127.0.0.1",
            displayName="somename",
            github='githuburls',
            profileImage='somesrc'
        )

        self.like = LikeModel.objects.create(
            summary='summary',
            actor=self.author,
            author=self.author,
            at_context='context'
        )

    def testActor(self):
        self.assertEquals(self.like.actor, self.author)

    def testObject(self):
        self.assertEquals(self.like.author, self.author)

    def testSummary(self):
        self.assertEquals(self.like.summary, 'summary')

    def testContent(self):
        self.assertEquals(self.like.at_context, 'context')


class TestInbox(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user",
            password="password123"
        )
        self.author = AuthorModel.objects.create(
            user=self.user,
            id='553b1321-00d5-43f1-8f5c-a1fe6ed63297',
            host="127.0.0.1",
            displayName="somename",
            github='githuburls',
            profileImage='somesrc'
        )

        self.inbox = InboxModel.objects.create(
            author=self.author,
            id=123
        )

    def testId(self):
        self.assertEquals(self.inbox.id, 123)


class TestFollowers(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user",
            password="password123"
        )

        self.followers = FollowersModel.objects.create(
            id=123
        )

    def testId(self):
        self.assertEquals(self.followers.id, 123)


class TestFollowerRequest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user",
            password="password123"
        )

        self.author = AuthorModel.objects.create(
            user=self.user,
            id='553b1321-00d5-43f1-8f5c-a1fe6ed63297',
            host="127.0.0.1",
            displayName="somename",
            github='githuburls',
            profileImage='somesrc'
        )

        self.follower_request =FollowRequestModel.objects.create(
            summary =  'summary',
            actor  = self.author,
            object  = self.author
        )

    def testSummary(self):
        self.assertEquals(self.follower_request.summary, 'summary')

    def testActor(self):
        self.assertEquals(self.follower_request.actor, self.author)

    def testObject(self):
        self.assertEquals(self.follower_request.object, self.author)




