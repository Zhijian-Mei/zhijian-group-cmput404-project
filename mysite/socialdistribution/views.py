from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import LoginInformationModel,AuthorModel


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
    return render(request,"service/myPostPage.html")


def myProfile(request):
    id = request.GET.get('id')
    displayName = AuthorModel.objects.get(id = id).displayName
    return render(request,"service/myProfile.html", {'id':id,'displayName':displayName})