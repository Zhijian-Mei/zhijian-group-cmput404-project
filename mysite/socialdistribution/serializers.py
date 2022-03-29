from socialdistribution.models import *
from rest_framework import serializers
import uuid

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['id', 'host', 'displayName', 'github', 'profileImage']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorModel.id
    author_object = AuthorSerializer()
    class Meta:
        # TODO commentsSrc
        model = PostModel
        fields = ['title', 'id', 'source', 'origin', 'description', 'contentType','content','image','image_src','author','author_object','categories','like_count','comments','published','visibility','unlisted']

class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareModel
        fields = ['author','post','author_name']
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        # TODO commentsSrc
        model = CommentModel
        fields = ['id', 'author', 'post', 'comment', 'contentType', 'published']

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        # TODO commentsSrc
        model = FollowRequestModel
        fields = ['summary', 'accept', 'actor_id', 'object_id']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = ['at_context','object','summary','actor_id','author_id']
