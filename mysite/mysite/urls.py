"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('service/', include('socialdistribution.urls')),
    path('',views.index),
    path('',include("django.contrib.auth.urls")),
    path('myprofile/',views.my_profile),
    path('mypost/',views.my_post),
    path('mypost/create/',views.create_post, name='createpost'),
    path('admin/', admin.site.urls),
    path('view/',views.view_post, name='viewpost'),
    path('mypost/view/',views.view_post, name='viewpost'),
    path('like', views.like, name='like'),
    path('follow', views.follow, name='follow'),
    path('share', views.share, name='share'),
    path('mypost/delete', views.delete, name='delete'),
    path('mypost/<str:image_url>', views.show_image, name='image'),
    path('myrequest/', views.my_request),
    path('myrequest/befriend', views.befriend, name='befriend'),
    path('mysubscriptions/', views.my_subscriptions),
    path('friendonly/', views.friend_only),
    path('inbox/', views.like_and_share),
]
