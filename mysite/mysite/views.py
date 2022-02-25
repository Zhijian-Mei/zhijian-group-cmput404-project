from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render,redirect
import json

from socialdistribution import views

def index(request):
    if request.method == "GET":
        posts = views.post_list(request)
        posts_list = json.loads(json.dumps(posts.data))
        print('posts list::::::',posts_list)
        data = {'posts_list': posts_list}
        return render(request, "service/postsList.html", data)