from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
import json
import uuid, random
from pathlib import Path
import os
import requests
import json

from socialdistribution import views
from rest_framework import status
from rest_framework.response import Response
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
        # print('posts list::::::', posts_list)
        comments = views.mycomment_list(request)
        comments_list = json.loads(json.dumps(comments.data, cls=MyEncoder))
        #print('comments list::::::', comments_list)
        authors = views.author_list(request)
        authors_list = json.loads(json.dumps(authors.data, cls=MyEncoder))
        #print('authors list::::::', authors_list)
        data = {'posts_list': posts_list, 'comments_list': comments_list, 'authors_list': authors_list}
        print({'posts_list': posts_list})
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

def edit_profile(request, id):
    if request.method == "GET":
        data = views.myProfile(request, id).data
        return render(request, "editprofile.html", {'profile': data})
    if request.method == "POST":
        result = views.myProfile(request, id)
        print('error--------------', result)
        if (result.status_code != 201):
            # TODO redirect to GET response
            print('error--------------', result.data)
        else:
            # TODO success message
            print('SUCCESS!!!! successfully added the post')
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

def my_profile(request):
    if request.method == "GET" :
        id = str(request.user.authormodel.id)
        data = views.myProfile(request, id).data
        return render(request, "myprofile.html",  {'profile': data})
    if request.method == "POST":
        id = str(request.user.authormodel.id)
        result = views.myProfile(request,id)
        print('error--------------',result)
        if(result.status_code!=201):
            #TODO redirect to GET response
            print('error--------------',result.data)
        else:
            #TODO success message
            print('SUCCESS!!!! successfully commented the post')
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(request.path_info)






def my_request(request):
    if request.method == "GET":
        requests = views.myrequest_list(request)
        requests_list = json.loads(json.dumps(requests.data, cls=MyEncoder))

        friends = views.myfriend_list(request)
        friends_list = json.loads(json.dumps(friends.data, cls=MyEncoder))

        authors = views.author_list(request)
        authors_list = json.loads(json.dumps(authors.data, cls=MyEncoder))
        author = views.my_author(request)
        myauthor = json.loads(json.dumps(author.data, cls=MyEncoder))
        #print(myauthor)
        data = {'requests_list': requests_list, 'authors_list': authors_list, 'friends_list': friends_list, 'my': myauthor}
        return render(request, "friendrequest.html", data)

def unfriend(request):
    if request.method == "POST":
        print(33333333, request.POST)
        result = views.unFriend(request)
        print('error--------------', result)
        if (result.status_code != 201):
            # TODO redirect to GET response
            print('error--------------', result.data)
            return redirect('./')
        else:
            # TODO success message
            print('SUCCESS!!!! successfully be friend!')
            return redirect('./')

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
        if (result.status_code != 201):
            # TODO redirect to GET response
            print('error--------------', result.data)
            return JsonResponse(result.data, safe=False)
        else:
            # TODO success message
            print('SUCCESS!!!! successfully added the post')
            return JsonResponse(result.data, safe=False)


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
        if(result.status_code!=200):
            #TODO redirect to GET response
            print('error--------------',result.data)
            return JsonResponse(result.data,safe=False)
        else:
            #TODO success message
            print('SUCCESS!!!! successfully added the post')
            return JsonResponse(result.data,safe=False)
        #next = request.POST.get('next', '/')
        #return HttpResponseRedirect(next)

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
        result = views.sharePost(request)
        print('error--------------', result)
        if result.status_code != 201:
            # TODO redirect to GET response
            print('error--------------', result.data)
            return redirect('./')
        else:
            # TODO success message
            print('SUCCESS!!!! successfully share the post!')
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
        url = '{}/'.format(id) + 'posts/'
        try:
            r = requests.get(url, auth=('group_12', 'ed19a258d40fde6748f2b5635e32fa62a78ec9305b606aabb0ba3810b491972c'))
            # print('team13 posts url----------------------------------',url)
            for post in json.loads(r.content.decode("utf-8"))['items']:
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
            print('team13 exception----------------------',e)
        continue
    # print('\n\n\n\n\n111111\n\n\n\n',posts_list)
    return posts_list

def team13_contentType_adaptor(data):
    if data=="image/jpeg;base64":
        return "image"
    if data=="text/plain":
        return "text"

# def team13_comment(request, id):
#     url = 'https://socialdistribution-t13.herokuapp.com/api/v1/authors/'
    # if request.method == "POST":
    #     print(33333333, request.POST)
    #     result = views.delete_post(request)
    #     print('error--------------', result)
    #     if (result.status_code != 201):
    #         # TODO redirect to GET response
    #         print('error--------------', result.data)
    #         return redirect('./')
    #     else:
    #         # TODO success message
    #         print('SUCCESS!!!! successfully send the request!')
    #         return redirect('./')

def get_foreign_posts_t5(request):
    url = 'https://cmput404-w22-project-backend.herokuapp.com/service/'
    url = url + 'authors/'
    r = requests.get(url,auth=('proxy','proxy123!'))
    authors = json.loads(r.content)['items']
    author_number = len(authors)
    author_id_list = []
    for i in range(author_number):
        id = authors[i]['id'].split("/")[4]
        #print(id)
        author_id_list.append(id)
    url_base = url
    posts_list =[]
    for id in author_id_list:
        url = url_base
        url = url + id + '/posts/'
        r = requests.get(url,auth=('proxy','proxy123!'))
        for post in json.loads(r.content)['items']:
            author = post['author']
            author['host']='https://cmput404-w22-project-backend.herokuapp.com/'
            data={
                "from":"TEAM05",
                "type":"post",
                "title":post['title'],
                "id":str(post['id']),
                "source":'',
                "origin":'',
                "description":post['description'],
                "contentType":team13_contentType_adaptor(post['contentType']),
                "content":post['content'],
                "author":author,
                "categories":post['categories'],
                "count":post['count'],
                "likecount":post['likeCount'],
                "comments":post['comments'],
                "commentsSrc":post['commentsSrc'],
                "published":post['published'],
                "visibility":post['visibility'],
                "unlisted":post['unlisted'],
            }
            #print(data)
            posts_list.append(data)
    # print('\n\n\n\n\n111111\n\n\n\n',posts_list)
    return posts_list

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
    # print('team11:data',data)
    return "markdown"
    if data=="text/plain":
        return "text"
    # elif data==""

def comment_adaptor(request):
    if request.method == "POST":
        # print(33333333, request.POST)
        # print('id---------------',list(request.POST)['id'])
        data = list(request.POST)
        return Response('comment', status=status.HTTP_201_CREATED)
        # result = views.delete_post(request)
        # print('error--------------', result)
        # if (result.status_code != 201):
        #     # TODO redirect to GET response
        #     print('error--------------', result.data)
        #     return redirect('./')
        # else:
        #     # TODO success message
        #     print('SUCCESS!!!! successfully send the request!')
        #     return redirect('./')
    if request.method == "GET":
        return Response(data, template_name='foreignpost.html')

def like_adaptor(request):
    if request.method == "POST":
        # print(33333333, request.POST)
        # print('id---------------',list(request.POST)['id'])
        data = list(request.POST)
        return Response('like', status=status.HTTP_201_CREATED)
        # result = views.delete_post(request)
        # print('error--------------', result)
        # if (result.status_code != 201):
        #     # TODO redirect to GET response
        #     print('error--------------', result.data)
        #     return redirect('./')
        # else:
        #     # TODO success message
        #     print('SUCCESS!!!! successfully send the request!')
        #     return redirect('./')def comment_adaptor(request):
    if request.method == "GET":
        return redirect('foreign_posts/')

def share_adaptor(request):
    if request.method == "POST":
        # print(33333333, request.POST)
        # print('id---------------',list(request.POST)['id'])
        data = list(request.POST)
        return Response('like', status=status.HTTP_201_CREATED)
        # result = views.delete_post(request)
        # print('error--------------', result)
        # if (result.status_code != 201):
        #     # TODO redirect to GET response
        #     print('error--------------', result.data)
        #     return redirect('./')
        # else:
        #     # TODO success message
        #     print('SUCCESS!!!! successfully send the request!')
        #     return redirect('./')
    if request.method == "GET":
        return redirect('foreign_posts/')

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
    try:
        posts_list.extend(get_foreign_posts_t13(request))
    except:
        pass
    try:
        posts_list.extend(get_foreign_posts_t11(request))
    except:
        pass
    try:
        posts_list.extend(get_foreign_posts_t6(request))
    except:
        pass
    try:
        posts_list.extend(get_foreign_posts_t5(request))
    except:
        pass
    posts_list.sort(key=lambda x: x['published'], reverse=True)
    data = {'posts_list': posts_list}
    return render(request, "foreignpost.html", data)


def sharedPost_from_friend(request):
    if request.method == 'GET':
        result = views.get_friend_share_post(request)
        print('error--------------', result)
        # print(result.data['share_objects'])
        # print(result.data['post_objects'])
        # print(len(result.data['post_objects']))
        if (result.status_code != 200):
            # TODO redirect to GET response
            print('error--------------', result.data)
            return redirect('../')
        else:
            # TODO success message
            share_objects = result.data['share_objects']
            for i in range(len(share_objects)):
                share_objects[i]['post'] = result.data['post_objects'][i]
            share_objects = json.loads(json.dumps(share_objects, cls=MyEncoder))
            data = {'share_objects':share_objects}
            # print(data)
            print('SUCCESS!!!! successfully get these posts')
            return render(request,'sharedpost.html',data)


def get_likes(request):
    if request.method == 'GET':
        result = views.get_likes(request)
        print('error--------------', result)
        if (result.status_code != 200):
            # TODO redirect to GET response
            print('error--------------', result.data)
            return redirect('../')
        else:
            # TODO success message
            like_objects = json.loads(json.dumps(result.data, cls=MyEncoder))
            print('\n\n\n\n',like_objects,'\n\n\n\n')
            print('SUCCESS!!!! successfully get these posts')
            return render(request,'likereceived.html',like_objects)
