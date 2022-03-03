from django.db import models


class AuthorModel(models.Model):
    # type = models.CharField(max_length=200, default='author')
    id = models.CharField(max_length=200, primary_key=True)
    host = models.CharField(max_length=200)
    displayName = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    profileImage = models.CharField(max_length=200)



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

class CommentsSrcModel(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    post = models.CharField(max_length=200)

class CommentModel(models.Model):
    # type = models.CharField(max_length=200, default='comment')
    id = models.CharField(max_length=200, primary_key=True)
    author = models.ForeignKey(AuthorModel, verbose_name=("comment"), on_delete=models.CASCADE)
    commentsSrc = models.ForeignKey(CommentsSrcModel, verbose_name=("comments"), on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)
    contentType = models.CharField(max_length=200,default='text/markdown')
    published = models.CharField(max_length=200)


class LikeModel(models.Model):
    at_context = models.CharField(max_length=200)
    author = models.ForeignKey(AuthorModel, related_name=("author"), on_delete=models.CASCADE)
    actor = models.ForeignKey(AuthorModel, related_name=("actor"), on_delete=models.CASCADE)
    object = models.CharField(max_length=200)   # linked to an author's post

class InboxModel(models.Model):
    author = models.CharField(max_length=200)
    models.ForeignKey(PostModel, verbose_name=("inbox"), on_delete=models.CASCADE)





