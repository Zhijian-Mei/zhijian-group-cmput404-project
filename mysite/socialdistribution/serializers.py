from socialdistribution.models import *
from rest_framework import serializers
import uuid

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['id', 'host', 'displayName', 'github', 'profileImage']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorModel.id
    class Meta:
        # TODO commentsSrc
        model = PostModel
        fields = ['title', 'id', 'source', 'origin', 'description', 'contentType','content','author','categories','count','comments','published','visibility','unlisted']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['id', 'comment', 'published', 'author_id', 'post','contentType']


