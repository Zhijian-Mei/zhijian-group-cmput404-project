from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
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
        #TODO generate id for post, may change later
        UUID = str(uuid.uuid4())
        return render(request, "createpost.html", {'UUID': UUID})
    if request.method == "POST":
        result = views.create_post(request)
        print('error--------------',result)
        if(result.status_code!=201):
            #TODO redirect to GET response
            print('error--------------',result.data)
        else:
            #TODO success message
            print('SUCCESS!!!! successfully added the post')
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)