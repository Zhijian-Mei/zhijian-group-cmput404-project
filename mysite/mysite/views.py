from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
import json
import uuid, random
from pathlib import Path
import os
import requests
import json

from socialdistribution import views

from mysite.settings import BASE_DIR


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,uuid.UUID):
            return str(obj)
        return json.JSONEncoder.default(self,obj)


def index(request):
    if request.method == "GET":
        posts = views.post_list(request)
        posts_list = json.loads(json.dumps(posts.data, cls=MyEncoder))
        print('posts list::::::', posts_list)
        comments = views.mycomment_list(request)
        comments_list = json.loads(json.dumps(comments.data, cls=MyEncoder))
        #print('comments list::::::', comments_list)
        authors = views.author_list(request)
        authors_list = json.loads(json.dumps(authors.data, cls=MyEncoder))
        #print('authors list::::::', authors_list)
        data = {'posts_list': posts_list, 'comments_list': comments_list, 'authors_list': authors_list}
        return render(request, "home.html",data)
    if request.method == "POST":
        result = views.comment_post(request)
        print('error--------------',result)
        if(result.status_code!=201):
            #TODO redirect to GET response
            print('error--------------',result.data)
        else:
            #TODO success message
            print('SUCCESS!!!! successfully commented the post')
            return HttpResponseRedirect(request.path_info)

def my_subscriptions(request):
    if request.method == "GET":
        posts = views.subscribes_list(request)
        posts_list = json.loads(json.dumps(posts.data, cls=MyEncoder))
        print('subsribes list::::::', posts_list)
        comments = views.mycomment_list(request)
        comments_list = json.loads(json.dumps(comments.data, cls=MyEncoder))
        #print('comments list::::::', comments_list)
        authors = views.author_list(request)
        authors_list = json.loads(json.dumps(authors.data, cls=MyEncoder))
        #print('authors list::::::', authors_list)
        data = {'posts_list': posts_list, 'comments_list': comments_list, 'authors_list': authors_list}
        return render(request, "mysubscriptions.html",data)
    if request.method == "POST":
        result = views.comment_post(request)
        print('error--------------',result)
        if(result.status_code!=201):
            #TODO redirect to GET response
            print('error--------------',result.data)
        else:
            #TODO success message
            print('SUCCESS!!!! successfully commented the post')
            return HttpResponseRedirect(request.path_info)

def friend_only(request):
    if request.method == "GET":
        posts = views.friends_posts_list(request)
        posts_list = json.loads(json.dumps(posts.data, cls=MyEncoder))
        print('subsribes list::::::', posts_list)
        comments = views.mycomment_list(request)
        comments_list = json.loads(json.dumps(comments.data, cls=MyEncoder))
        print('comments list::::::', comments_list)
        authors = views.author_list(request)
        authors_list = json.loads(json.dumps(authors.data, cls=MyEncoder))
        #print('authors list::::::', authors_list)
        author_object = request.user.authormodel.id
        print('::::::::::::', request.user.authormodel.id)
        data = {'posts_list': posts_list, 'comments_list': comments_list, 'authors_list': authors_list, 'author_id': author_object}
        return render(request, "friendonly.html",data)
    if request.method == "POST":
        result = views.comment_post(request)
        print('error--------------',result)
        if(result.status_code!=201):
            #TODO redirect to GET response
            print('error--------------',result.data)
        else:
            #TODO success message
            print('SUCCESS!!!! successfully commented the post')
            return HttpResponseRedirect(request.path_info)

def like_and_share(request):
    return render(request, "new.html")

def my_post(request):
    if request.method == "GET":
        image = str(request.user.authormodel.profileImage)
        print(1235134513451234,image)
        posts = views.mypost_list(request)
        print('posts.data:',posts.data)
        posts_list = json.loads(json.dumps(posts.data, cls=MyEncoder))
        #print('posts list::::::', posts_list)
        comments = views.mycomment_list(request)
        comments_list = json.loads(json.dumps(comments.data, cls=MyEncoder))
        #print('comments list::::::', comments_list)
        authors = views.author_list(request)
        authors_list = json.loads(json.dumps(authors.data, cls=MyEncoder))
        data = {'posts_list': posts_list, 'comments_list': comments_list,'image':image, 'authors_list': authors_list}
        print('data:',data)
        return render(request, "mypost.html",data)
    if request.method == "POST":
        result = views.comment_post(request)
        print('error--------------',result)
        if(result.status_code!=201):
            #TODO redirect to GET response
            print('error--------------',result.data)
        else:
            #TODO success message
            print('SUCCESS!!!! successfully commented the post')
            return HttpResponseRedirect(request.path_info)

def my_profile(request):
    if request.method == "GET":
        return render(request, "myprofile.html")

def my_request(request):
    if request.method == "GET":
        requests = views.myrequest_list(request)
        requests_list = json.loads(json.dumps(requests.data, cls=MyEncoder))
        #print('requests list::::::', requests_list)
        authors = views.author_list(request)
        authors_list = json.loads(json.dumps(authors.data, cls=MyEncoder))
        data = {'requests_list': requests_list, 'authors_list': authors_list}
        return render(request, "friendrequest.html", data)


def befriend(request):
    if request.method == "POST":
        print(33333333, request.POST)
        result = views.beFriend(request)
        print('error--------------', result)
        if (result.status_code != 201):
            # TODO redirect to GET response
            print('error--------------', result.data)
            return redirect('./')
        else:
            # TODO success message
            print('SUCCESS!!!! successfully be friend!')
            return redirect('./')


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

def edit_post(request, id):
    """
    Edit an existing post
    """
    if request.method == "GET":
        data = views.edit_post(request,id).data
        # print('data-------------',data)
        #TODO solve the error if there's no such post
        return render(request, "editpost.html", {'post': data})
    if request.method == "POST":
        result = views.edit_post(request,id)
        print('error--------------',result)
        if(result.status_code!=201):
            #TODO redirect to GET response
            print('error--------------',result.data)
        else:
            #TODO success message
            print('SUCCESS!!!! successfully added the post')
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

def view_post(request):
    if request.method == "GET":
        return render(request, "textpost.html")

def like(request):
    if request.method == "POST":
        result = views.like_post(request)
        print('error--------------', result)
        if result.status_code != 201:
            # TODO redirect to GET response
            print('error--------------', result.data)
            return redirect('./')
        else:
            # TODO success message
            print('SUCCESS!!!! successfully like the post!')
            return redirect('./')


def follow(request):
    if request.method == "POST":
        result = views.followFriendRequest(request)
        print('error--------------', result)
        if (result.status_code != 201):
            # TODO redirect to GET response
            print('error--------------', result.data)
            return redirect('./')
        else:
            # TODO success message
            print('SUCCESS!!!! successfully send the request!')
            return redirect('./')


def share(request):
    if request.method == "POST":
        print(33333333, request.POST)
        return redirect('./')

def delete(request):
    if request.method == "POST":
        print(33333333, request.POST)
        result = views.delete_post(request)
        print('error--------------', result)
        if (result.status_code != 201):
            # TODO redirect to GET response
            print('error--------------', result.data)
            return redirect('./')
        else:
            # TODO success message
            print('SUCCESS!!!! successfully send the request!')
            return redirect('./')

def show_image(request,image_url):
    print(request,image_url)
    path = os.path.join(BASE_DIR,'mysite/img/',image_url)
    print('path: ',path)
    image = open(path,"rb")
    return HttpResponse(image.read(),content_type='image/jpg')

def get_foreign_posts_t13(request):
    url = 'https://socialdistribution-t13.herokuapp.com/api/v1/'
    url = url + 'authors/'
    r = requests.get(url,auth=('group_12','ed19a258d40fde6748f2b5635e32fa62a78ec9305b606aabb0ba3810b491972c'))
    authors = json.loads(r.content)['items']
    author_number = len(authors)
    author_id_list = []
    for i in range(author_number):
        author_id_list.append(authors[i]['id'])
    url_base = url
    posts_list =[]
    for id in author_id_list:
        url = url_base
        url = url + '{}/'.format(id) + 'posts/'
        try:
            r = requests.get(url, auth=('group_12', 'ed19a258d40fde6748f2b5635e32fa62a78ec9305b606aabb0ba3810b491972c'),timeout=5)
            for post in json.loads(r.content)['items']:
                author = post['author']
                author['host']='https://socialdistribution-t13.herokuapp.com/'
                data={
                    "from":"TEAM13",
                    "type":"post",
                    "title":post['title'],
                    "id":str(post['id']),
                    "source":post['source'],
                    "origin":post['origin'],
                    "description":post['description'],
                    "contentType":team13_contentType_adaptor(post['contentType']),
                    "content":post['content'],
                    "author":author,
                    "categories":post['categories'],
                    "count":post['count'],
                    "comments":'',
                    "commentsSrc":{
                        "type":"comments",
                        "page":0,
                        'size':0,
                        'post':'',
                        'id':'',
                        'comments':[]
                    },
                    "published":post['published'],
                    "visibility":post['visibility'],
                    "unlisted":post['unlisted'],
                }
                posts_list.append(data)
        except Exception as e:
            pass
        continue
    print('\n\n\n\n\n111111\n\n\n\n',posts_list)
    return posts_list

def team13_contentType_adaptor(data):
    if data=="image/jpeg;base64":
        return "image"
    if data=="text/plain":
        return "text"

    

def get_foreign_posts_t11(request):
    url = 'https://psdt11.herokuapp.com/authors/'
    r = requests.get(url, auth=('team12', 'team12'))
    authors = json.loads(r.content)['items']
    posts_list = []
    for author in authors:
        url = author['url'] + '/posts/'
        try:
            r = requests.get(url, auth=('team12', 'team12'),timeout=5)
            for post in json.loads(r.content)['items']:
                posts_list.append({
                    "from": "TEAM11",
                    "type": "post",
                    "title": post['title'],
                    "id": str(post['id']),
                    "source": '',
                    "origin": '',
                    "description": post['description'],
                    "contentType": team11_contentType_adaptor(post['content_type']),
                    "content": post['content'],
                    "author": post['author'],
                    "categories": '',
                    "count": post['count'],
                    "comments": post['comments'],
                    "commentsSrc": post['comment_src'],
                    "published": post['published'],
                    "visibility": post['visibility'],
                    "unlisted": post['unlisted'],
                })
        except Exception as e:
            pass
        continue
    # print(22222,posts_list)
    return posts_list


def team11_contentType_adaptor(data):
    if data=="text/plain":
        return "text"

def get_foreign_posts_t6(request):
    url = 'http://team06-backend-social-dist.herokuapp.com/posts/'
    r = requests.get(url, auth=('team12', 'cmput404'))
    posts = json.loads(r.content)['items']
    posts_list = []
    for post in posts:
        contentType = post['content']
        if contentType=="text/plain":
            contentType="text"
        commentSrc = post['commentsSrc']
        commentSrc['type']='comments'
        commentSrc['id']=''
        commentSrc['post']=''
        posts_list.append({
            "from":"TEAM6",
            "type":"post",
            "title":post['title'],
            "id":post['id'],
            "source":post['source'],
            "origin":post['origin'],
            "description":post['description'],
            "contentType":contentType,
            "content":post['content'],
            "author":post['author'],
            "categories":post['categories'],
            "count":post['count'],
            "comments":post['comments'],
            "commentsSrc":commentSrc,
            "published":post['published'],
            "visibility":post['visibility'],
            "unlisted":post['unlisted'],
        })
    # print('\n\n\nt6\n\n\n\n',posts_list)
    return posts_list

def get_foreign_posts(request):
    posts_list = []
    posts_list.extend(get_foreign_posts_t13(request))
    posts_list.extend(get_foreign_posts_t11(request))
    posts_list.extend(get_foreign_posts_t6(request))
    posts_list.sort(key=lambda x: x['published'], reverse=True)
    data = {'posts_list': posts_list}
    return render(request, "foreignpost.html", data)