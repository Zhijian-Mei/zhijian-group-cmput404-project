from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render,redirect


def index(request):
    return HttpResponse("Hello, world.")

def login(request):
    if request.method == "GET":
        return render(request,"service/login.html")
    username = request.POST.get('user')
    password = request.POST.get('pwd')
    print(username,password)
    if username == '123' and password == '123':
        return redirect('http://www.baidu.com')
    return render(request,"service/login.html",{'error_msg' : 'Incorrect Username or Password!'})