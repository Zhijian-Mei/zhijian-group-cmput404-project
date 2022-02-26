from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_authors(request):
    """
    GET and return all authors
    """
    if request.method == 'GET':
        authors = AuthorModel.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        data = {"type": "authors",
        "items":serializer.data
        }
        return Response(data)

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
        posts = PostModel.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
        # serializer = PostSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_post(request):
    """
    Create a new Post
    """
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        print("api received request data:    ",request.data)
        # print("\n\nauthor type/id type:   ",type(request.data['author']),type(request.data['id']))
        #TODO add author inside, how???
        if serializer.is_valid(raise_exception=True):
            # TODO, this Hard code way, try to change serializer
            author_object = AuthorModel.objects.get(id=request.data['author'])
            serializer.author = author_object
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return HttpResponse("Hello, world.")

def login(request):
    if request.method == "GET":
        return render(request,"service/login.html")
    username = request.POST.get('user')
    password = request.POST.get('pwd')
    try:
        record = LoginInformationModel.objects.get(username=username)
    except:
        record = None
    if record is None:
        return render(request,"service/login.html",{'error_msg' : 'Incorrect Username or Password!'})
    if password == record.password:
        id = record.id


        return redirect('http://127.0.0.1:8000/service/myProfile/?id={}'.format(id))
    else:
        return render(request, "service/login.html", {'error_msg': 'Incorrect Username or Password!'})


def myPostPage(request):
    id = request.GET.get('id')
    displayName = AuthorModel.objects.get(id=id).displayName
    return render(request,"service/myPostPage.html",{'id':id,'displayName':displayName})


def myProfile(request):
    id = request.GET.get('id')
    displayName = AuthorModel.objects.get(id = id).displayName
    return render(request,"service/myProfile.html", {'id':id,'displayName':displayName})
