from django.shortcuts import render

from django.http import HttpResponse


from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import uuid, random
from datetime import datetime

@api_view(['GET'])
def get_authors(request):
    """
    GET and return all authors
    """
    if request.method == 'GET':
        authors = AuthorModel.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        data = {"type": "authors",
                "items": serializer.data
                }
        return Response(data)

@api_view(['GET'])
def get_post(request,post_id,author_id):
    """
        GET and return a post
        """
    if request.method == 'GET':
        #print(post_id)
        try:
            post = PostModel.objects.get(id=post_id)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        # TODO polish error message
        except Exception as e:
            data = {'error': str(e)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_author(request, author_id):
    """
    GET and return specific author
    """
    if request.method == 'GET':
        try:
            author = AuthorModel.objects.get(id=author_id)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        # TODO polish error message
        except Exception as e:
            data = {'error': str(e)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def post_list(request):
    """
    List all Posts
    """
    if request.method == 'GET':
        posts = PostModel.objects.order_by('-published')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def mypost_list(request):
    """
    List all Posts
    """
    if request.method == 'GET':
        posts = PostModel.objects.order_by('-published')
        posts = posts.filter(author=request.user.authormodel)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def create_post(request):
    """
    Create a new Post
    """
    if request.method == 'POST':
        print("api received request data:    ", request.data)
        data = request.data
        author_object = AuthorModel.objects.get(id=data['author'])
        unlisted = False
        if 'unlisted' in data.keys():
            unlisted = True
        try:
            PostModel.objects.create(title=data['title'], id=data['id'], source=data['source'], origin=data['origin'],
                                     description=data['description'], contentType=data['contentType'],
                                     content=data['content'], author=author_object,
                                     categories=data['categories'], visibility=data['visibility'], unlisted=unlisted)
            message = {'message:', 'successfully created post'}
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            message = {'error:', e}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def followFriendRequest(request):
    """
    Send a new request for being friends or just follow
    """
    if request.method == 'POST':
        print("api received request data:    ", request.data)
        data = request.data
        try:
            FollowRequest = FollowRequestModel.objects.filter(object_id = data['authorID'])
            FollowRequest = FollowRequest.filter(actor_id = request.user.authormodel.id)
            if FollowRequest:
                return Response('Cannot resend follow request!!!!', status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        object = AuthorModel.objects.get(id=data['authorID'])
        actor = AuthorModel.objects.get(id=request.user.authormodel.id)
        if actor == object:
            return Response('Cannot follow yourself!!!!', status=status.HTTP_400_BAD_REQUEST)
        try:
            FollowRequestModel.objects.create(summary='{0} wants to follow {1}'.format(actor.displayName,object.displayName),
                                              actor=actor,object=object
                                              )
            message = {'message:', 'successfully send request'}
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            message = {'error:', e}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def like_post(request):
    """
    Send a new like object to author's post
    """
    if request.method == 'POST':
        print("api received request data:    ", request.data)
        data = request.data
        author = AuthorModel.objects.get(id=data['authorID'])
        post_url = author.host + 'service/authors/' + str(author.id) + '/posts/' + request.POST['object']
        try:
            like_object = LikeModel.objects.filter(actor_id = request.user.authormodel.id)
            like_object = like_object.filter(object=post_url)
            print(like_object)
            if like_object:
                return Response('Cannot re-like same post !!!!', status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
        object = AuthorModel.objects.get(id=data['authorID'])
        actor = AuthorModel.objects.get(id=request.user.authormodel.id)
        try:
            LikeModel.objects.create(summary="{0} likes {1}'s post".format(actor.displayName,object.displayName),
                                              actor=actor,author=object,object=post_url,at_context='content'
                                              )
            message = {'message:', 'successfully like this post'}
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            message = {'error:', e}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def comment_post(request):
    """
    Comment a Post
    """
    if request.method == 'POST':
        print("api received request data:    ", request.data)
        data = request.data
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            CommentModel.objects.create(comment=data['comment'], post=data['postID'], author_id=request.user.authormodel.id, published=dt_string,
                                        id=uuid.uuid4())
            message = {'message:', 'successfully commented post'}
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            message = {'error:', e}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)




def index(request):
    return HttpResponse("Hello, world.")


def view_post(request):
    if request.method == "GET":
        return render(request, "textpost.html")

def get_comments(request):
    if request.method == "GET":
        comments = CommentModel.objects.filter(post=request.GET['id'])
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)