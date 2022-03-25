from logging import exception
from django.shortcuts import render
from django.db.models import Q

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import uuid, random
from datetime import datetime
from .forms import UserUpdateForm, ProfileUpdateForm


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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def post_list(request):
    """
    List all Posts
    """
    if request.method == 'GET':
        posts = PostModel.objects.order_by('-published')
        posts = posts.filter(visibility='PUBLIC')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    # serializer = PostSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #


@api_view(['GET', 'POST'])
def author_list(request):
    """
    List all Authors
    """
    if request.method == 'GET':
        authors = AuthorModel.objects.order_by('-displayName')
        serializer = AuthorSerializer(authors, many=True)
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


@api_view(['GET', 'POST'])
def subscribes_list(request):
    """
    List all Subscriptions
    """
    if request.method == 'GET':
        subscriptions = FollowRequestModel.objects.order_by('-summary')
        subscriptions_1 = subscriptions.filter(actor_id=request.user.authormodel)
        subscriptions_2 = subscriptions.filter(object_id=request.user.authormodel, accept=1)
        subscribers_id1 = set(subscription.object_id for subscription in subscriptions_1)
        subscribers_id2 = set(subscription.actor_id for subscription in subscriptions_2)
        # TODO: add friends' public posts
        posts = PostModel.objects.order_by('-published')
        posts = posts.filter((Q(author__in=subscribers_id1) | Q(author__in=subscribers_id2)), visibility='PUBLIC')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def friends_posts_list(request):
    """
    List all Friends' Posts
    """
    if request.method == 'GET':
        friends = FollowRequestModel.objects.order_by('-summary')
        friends_1 = friends.filter(actor_id=request.user.authormodel, accept=1)
        friends_2 = friends.filter(object_id=request.user.authormodel, accept=1)
        friends_id1 = set(friend.object_id for friend in friends_1)
        friends_id2 = set(friend.actor_id for friend in friends_2)
        # TODO: add friends' public posts
        posts = PostModel.objects.order_by('-published')
        posts = posts.filter((Q(author__in=friends_id1) | Q(author__in=friends_id2)), visibility='FRIEND')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def mycomment_list(request):
    """
    List all Comments
    """
    if request.method == 'GET':
        comments = CommentModel.objects.order_by('-published')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def myrequest_list(request):
    """
    List all Comments
    """
    if request.method == 'GET':
        followers = FollowRequestModel.objects.order_by('-summary')
        followers = followers.filter(object_id=request.user.authormodel)
        followers = followers.filter(accept=0)
        serializer = FollowerSerializer(followers, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def beFriend(request):
    if request.method == 'POST':
        actor_id = request.POST['actor_id']
        object_id = request.POST['object_id']
        try:
            request = FollowRequestModel.objects.get(object_id=object_id, actor_id=actor_id)
            request.accept = 1
            request.save()
            message = {'message:', 'successfully be friend'}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = {'error:', e}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_post(request):
    """
    Create a new Post
    """
    if request.method == 'POST':
        # serializer = PostSerializer(data=request.data)
        # # print("\n\nauthor type/id type:   ",type(request.data['author']),type(request.data['id']))
        # #TODO add author inside, how???
        # if serializer.is_valid(raise_exception=True):
        #     # TODO, this Hard code way, try to change serializer
        #     author_object = AuthorModel.objects.get(id=request.data['author'])
        #     serializer.author = author_object
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print("api received request data:    ", request.data)
        data = request.data
        author_object = AuthorModel.objects.get(id=data['author'])
        unlisted = False
        if 'unlisted' in data.keys():
            unlisted = True
        try:
            PostModel.objects.create(title=data['title'], id=data['id'], source=data['source'], origin=data['origin'],
                                     description=data['description'], contentType=data['contentType'],
                                     content=data['content'], image_src=data['imagesrc'], image=data['image'],
                                     author=author_object,
                                     categories=data['categories'], visibility=data['visibility'], unlisted=unlisted)
            message = {'message:', 'successfully created post'}
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            message = {'error:', e}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def edit_post(request, id):
    """
    Create a new Post
    """
    if request.method == 'GET':
        try:
            post_object = PostModel.objects.get(id=id)
            post = {
                'title': post_object.title,
                'description': post_object.description,
                'contentType': post_object.contentType,
                'content': post_object.content,
                'image': post_object.image,
                'imagesrc': post_object.image_src,
                'categories': post_object.categories,
                'visibility': post_object.visibility,
                'unlisted': post_object.unlisted,
            }
            return Response(post, status=status.HTTP_200_OK)
        except Exception as e:
            message = {'error:', e}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        print("api received request data:    ", request.data)
        data = request.data
        unlisted = False
        if 'unlisted' in data.keys():
            unlisted = True
        try:
            PostModel.objects.filter(id=id).update(title=data['title'], description=data['description'],
                                                   contentType=data['contentType'],
                                                   content=data['content'], image=data['image'],
                                                   image_src=data['imagesrc'], categories=data['categories'],
                                                   visibility=data['visibility'], unlisted=unlisted)
            message = {'message:', 'successfully updated post'}
            return Response(message, status=status.HTTP_200_OK)
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
            print('::::', data['postID'])
            CommentModel.objects.create(comment=data['comment'], post_id=data['postID'],
                                        author_id=request.user.authormodel.id, published=dt_string,
                                        id=uuid.uuid4())
            message = {'message:', 'successfully commented post'}
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            message = {'error:', e}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return HttpResponse("Hello, world.")


def login(request):
    if request.method == "GET":
        return render(request, "service/login.html")
    username = request.POST.get('user')
    password = request.POST.get('pwd')
    try:
        record = LoginInformationModel.objects.get(username=username)
    except:
        record = None
    if record is None:
        return render(request, "service/login.html", {'error_msg': 'Incorrect Username or Password!'})
    if password == record.password:
        id = record.id

        return redirect('http://127.0.0.1:8000/service/myProfile/?id={}'.format(id))
    else:
        return render(request, "service/login.html", {'error_msg': 'Incorrect Username or Password!'})


def myPostPage(request):
    id = request.GET.get('id')
    displayName = AuthorModel.objects.get(id=id).displayName
    return render(request, "service/myPostPage.html", {'id': id, 'displayName': displayName})


def myProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.authormodel)
        p_form = ProfileUpdateForm(request.authormodel
                                   )

        if not u_form.is_valid() or not p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated ')
            return redirect('myProfile')
    else:
        u_form = UserUpdateForm(request.authormodel)
        p_form = ProfileUpdateForm(request.authormodel)

    content = {
        'u-form': u_form,
        'p-form': p_form
    }
    return render(request, "service/myProfile.html", content)


def view_post(request):
    if request.method == "GET":
        return render(request, "textpost.html")


@api_view(['POST'])
def followFriendRequest(request):
    """
    Send a new request for being friends or just follow
    """
    if request.method == 'POST':
        # print("api received request data:    ", request.data)
        data = request.data
        try:
            FollowRequest = FollowRequestModel.objects.filter(object_id=data['authorID'])
            FollowRequest = FollowRequest.filter(actor_id=request.user.authormodel.id)
            if FollowRequest:
                return Response('Cannot resend follow request!!!!', status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        object = AuthorModel.objects.get(id=data['authorID'])
        actor = AuthorModel.objects.get(id=request.user.authormodel.id)
        if actor == object:
            return Response('Cannot follow yourself!!!!', status=status.HTTP_400_BAD_REQUEST)
        try:
            FollowRequestModel.objects.create(
                summary='{0} wants to follow {1}'.format(actor.displayName, object.displayName),
                actor=actor, object=object
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
        # print("api received request data:    ", request.data)
        data = request.data
        author = AuthorModel.objects.get(id=data['authorID'])
        post_url = author.host + 'service/authors/' + str(author.id) + '/posts/' + request.POST['object']
        try:
            like_object = LikeModel.objects.filter(actor_id=request.user.authormodel.id)
            like_object = like_object.filter(object=post_url)
            if like_object:
                return Response('Cannot re-like same post !!!!', status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
        object = AuthorModel.objects.get(id=data['authorID'])
        actor = AuthorModel.objects.get(id=request.user.authormodel.id)
        post = PostModel.objects.get(id=request.POST['object'])
        try:
            LikeModel.objects.create(summary="{0} likes {1}'s post".format(actor.displayName, object.displayName),
                                     actor=actor, author=object, object=post_url, at_context='content'
                                     )
            post = PostModel.objects.get(id=data['object'])
            like_count = post.like_count
            post.like_count = like_count + 1
            post.save()
            message = {'message:', 'successfully like this post'}
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            message = {'error:', e}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


def delete_post(request):
    if request.method == 'POST':
        # print("api received request data:    ", request.data)
        post_id = request.POST['post_id']
        try:
            PostModel.objects.get(id=post_id).delete()
            message = {'message:', 'successfully delete this post'}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = {'error:', e}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_author_followers(request, author_id):
    if request.method == 'GET':
        try:
            followers = FollowRequestModel.objects.all()
            followers = followers.filter(object_id=author_id)
            followers = list({}.fromkeys([follower.actor_id for follower in followers]).keys())
            followers_list = []
            for follower in followers:
                author = AuthorModel.objects.get(id=follower)
                followers_list.append(author)
            serializer = AuthorSerializer(followers_list, many=True)
            return Response(serializer.data)
        except Exception as e:
            data = {'error': str(e)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_author_posts(request,author_id):
    if request.method == 'GET':
        posts = PostModel.objects.order_by('-published')
        posts = posts.filter(author_id=author_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_author_post(request,author_id,post_id):
    if request.method == 'GET':
        posts = PostModel.objects.get(id=post_id)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post_comments(request,author_id,post_id):
    if request.method == 'GET':
        comments = CommentModel.objects.all()
        comments = comments.filter(post_id=post_id)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post_likes(request,author_id,post_id):
    if request.method == 'GET':
        likes = LikeModel.objects.all()
        object = request.scheme + '://'+request.get_host() + '/service/authors/' + str(author_id) + '/posts/' + post_id
        likes = likes.filter(object=object)
        serializer = LikeSerializer(likes,many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_author_liked(request,author_id):
    if request.method == 'GET':
        likes = LikeModel.objects.all()
        likes = likes.filter(actor_id=author_id)
        serializer = LikeSerializer(likes, many=True)
        print(12312312,serializer.data)
        return Response(serializer.data)

