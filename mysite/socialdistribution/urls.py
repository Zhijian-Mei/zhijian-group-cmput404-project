from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login),
    path('myPostPage/',views.myPostPage),
    path('myProfile/',views.myProfile),
    path('post/',views.post_list),
    path('createpost/',views.create_post,name='api_createpost'),
]