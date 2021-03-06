from PIL import Image
from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth.models import User

class AuthorModel(models.Model):
    # type = models.CharField(max_length=200, default='author')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField(max_length=200, default=settings.HOST_URL)
    displayName = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    profileImage = models.ImageField(verbose_name='profile_image',upload_to='',null=True)




class FollowersModel(models.Model):
    # type = models.CharField(max_length=200, default='followers')
    items = models.ManyToManyField(AuthorModel)

class FollowRequestModel(models.Model):
    # type = models.CharField(max_length=200, default='Follow')
    summary = models.CharField(max_length=200)
    actor = models.ForeignKey(AuthorModel, related_name=("follower"), on_delete=models.CASCADE)
    object = models.ForeignKey(AuthorModel, related_name=("followee"), on_delete=models.CASCADE)
    accept = models.BooleanField(default=False)

class PostModel(models.Model):
    # type = models.CharField(max_length=200, default='post')
    title = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)
    source = models.CharField(max_length=200, blank=True)
    origin = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200)
    contentType = models.CharField(max_length=200)
    content = models.CharField(max_length=2000, blank=True)
    image = models.ImageField(verbose_name='post_image',upload_to='',null=True)
    image_src = models.CharField(max_length=2000, blank=True)
    author = models.ForeignKey(AuthorModel, related_name=("post"), on_delete=models.CASCADE, null=True)
    author_object = models.ForeignKey(AuthorModel, related_name=("post_obj"), on_delete=models.CASCADE, null=True)
    categories = models.CharField(max_length=200)
    like_count = models.IntegerField(default=0)
    comments = models.CharField(max_length=200, blank=True)
    published = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=200)
    unlisted = models.BooleanField()



    class Mate:
        ordering = ['-published']

class CommentModel(models.Model):
    # type = models.CharField(max_length=200, default='comment')
    id = models.CharField(max_length=200, primary_key=True)
    author = models.ForeignKey(AuthorModel, related_name=("comment_name"), on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, related_name=("comments_set"), on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)
    contentType = models.CharField(max_length=200)
    published = models.CharField(max_length=200)


class LikeModel(models.Model):
    at_context = models.CharField(max_length=200)
    author = models.ForeignKey(AuthorModel, related_name=("author"), on_delete=models.CASCADE)
    actor = models.ForeignKey(AuthorModel, related_name=("actor"), on_delete=models.CASCADE)
    object = models.CharField(max_length=200)   # linked to an author's posts and comments
    summary = models.CharField(max_length=200)

class ShareModel(models.Model):
    author_name = models.CharField(max_length=200,default='authorName')
    author = models.ForeignKey(AuthorModel, related_name=('Sharer'),on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel,related_name=('Shared_post'), on_delete=models.CASCADE)

class InboxModel(models.Model):
    author = models.CharField(max_length=200)
    models.ForeignKey(PostModel, related_name=("inbox"), on_delete=models.CASCADE)

class LoginInformationModel(models.Model):
    username = models.CharField(max_length=30, verbose_name='username')
    password = models.CharField(max_length=30, verbose_name='password')
    id = models.CharField(max_length=300,verbose_name='id',primary_key=True)

    class Meta:
        db_table = 'LoginInformation'

