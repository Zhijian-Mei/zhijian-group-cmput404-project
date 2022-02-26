from socialdistribution.models import *
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['id', 'host', 'displayName', 'github', 'profileImage']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        # TODO commentsSrc
        model = PostModel
        fields = ['title', 'id', 'source', 'origin', 'description', 'contentType','content','author','categories','count','comments','published','visibility','unlisted']
