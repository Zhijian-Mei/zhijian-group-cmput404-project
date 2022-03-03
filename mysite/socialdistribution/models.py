from django.db import models


class AuthorModel(models.Model):
    # type = models.CharField(max_length=200, default='author')
    id = models.CharField(max_length=200, primary_key=True)
    host = models.CharField(max_length=200)
    displayName = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    profileImage = models.CharField(max_length=200)



class FollowersModel(models.Model):
    # type = models.CharField(max_length=200, default='followers')
    items = models.ManyToManyField(AuthorModel)

class FollowRequestModel(models.Model):
    # type = models.CharField(max_length=200, default='Follow')
    summary = models.CharField(max_length=200)
    actor = models.ForeignKey(FollowersModel, verbose_name=("follower"), on_delete=models.CASCADE)
    object = models.ForeignKey(AuthorModel, verbose_name=("followee"), on_delete=models.CASCADE)

class PostModel(models.Model):
    # type = models.CharField(max_length=200, default='post')
    title = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)
    source = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    contentType = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    author = models.ForeignKey(AuthorModel, verbose_name=("post"), on_delete=models.CASCADE)
    categories = models.CharField(max_length=200)
    count = models.IntegerField()
    comments = models.CharField(max_length=200)
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


class LikedModel(models.Model):
    at_context = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    author = models.ForeignKey(AuthorModel, verbose_name=("liked"), on_delete=models.CASCADE)
    object = models.CharField(max_length=200)   # linked to an author's post

class InboxModel(models.Model):
    author = models.CharField(max_length=200)
    models.ForeignKey(PostModel, verbose_name=("inbox"), on_delete=models.CASCADE)

class LoginInformationModel(models.Model):
    username = models.CharField(max_length=30, verbose_name='username')
    password = models.CharField(max_length=30, verbose_name='password')
    id = models.CharField(max_length=300,verbose_name='id',primary_key=True)

    class Meta:
        db_table = 'LoginInformation'
