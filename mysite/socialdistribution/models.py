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
    items = models.ForeignKey(AuthorModel, verbose_name=("followers"), on_delete=models.CASCADE)

class FollowRequestModel(models.Model):
    # type = models.CharField(max_length=200, default='Follow')
    summary = models.CharField(max_length=200)
    actor = models.OneToOneField(
        AuthorModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    object = models.OneToOneField(
        AuthorModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class PostModel(models.Model):
    # type = models.CharField(max_length=200, default='post')
    title = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)
    source = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    contentType = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    author = models.OneToOneField(
        AuthorModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    categories = models.CharField(max_length=200)
    count = models.IntegerField()
    comments = models.CharField(max_length=200)
    # commentsSrc = ?
    published = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=200)
    unlisted = models.BooleanField()

class CommentModel(models.Model):
    # type = models.CharField(max_length=200, default='comment')
    id = models.CharField(max_length=200, primary_key=True)
    author = models.OneToOneField(
        AuthorModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    comment = models.CharField(max_length=2000)
    contentType = models.CharField(max_length=200)
    published = models.CharField(max_length=200)

class LikedModel(models.Model):
    at_context = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    author = models.OneToOneField(
        AuthorModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    object = models.CharField(max_length=200)

class InboxModel(models.Model):
    author = models.CharField(max_length=200)
    models.ForeignKey(PostModel, verbose_name=("inbox"), on_delete=models.CASCADE)


