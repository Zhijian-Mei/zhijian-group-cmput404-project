from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render,redirect
import json
import uuid, random

from socialdistribution import views

def index(request):
    if request.method == "GET":
        posts = views.post_list(request)
        posts_list = json.loads(json.dumps(posts.data))
        print('posts list::::::',posts_list)
        data = {'posts_list': posts_list}
        return render(request, "home.html", data)

def my_post(request):
    if request.method == "GET":
        return render(request, "mypost.html")

def my_profile(request):
    if request.method == "GET":
        return render(request, "myprofile.html")

def create_post(request):
    """
    Create a new Post
    """
    if request.method == "GET":
        #TODO generate id for post, need to change later
        UUID = uuid.uuid1(random.randint(0, 281474976710655))
        return render(request, "createpost.html", {'UUID': UUID})
    if request.method == "POST":
        result = views.create_post(request)
        print('error--------------',result)
        if(result.status_code!=201):
            #TODO redirect to GET
            print('error--------------',result.data)
        else:
            #TODO success message
            print('SUCCESS!!!! successfully added the post')
        return render(request, "createpost.html")