from socialdistribution.models import *
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['id', 'host', 'displayName', 'url', 'github', 'profileImage']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # TODO commentsSrc
        model = PostModel
        fields = ['title', 'id', 'source', 'origin', 'description', 'contentType','content','author','categories','count','comments','published','visibility','unlisted']
