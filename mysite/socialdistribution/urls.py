from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login),
    path('myPostPage/',views.myPostPage),
    path('myProfile/<str:id>',views.myProfile),
    path('post/',views.post_list),
    path('createpost/',views.create_post,name='api_createpost'),
    path('editpost/<str:id>',views.edit_post,name='api_editpost'),
    path('authors/',views.get_authors),
    path('authors/<str:author_id>',views.get_author),
    path('authors/<str:author_id>/followers',views.get_author_followers),
    path('authors/<str:author_id>/posts',views.get_author_posts),
    path('authors/<str:author_id>/posts/<str:post_id>',views.get_author_post),
    path('authors/<str:author_id>/posts/<str:post_id>/comments',views.get_post_comments),
    path('authors/<str:author_id>/posts/<str:post_id>/likes',views.get_post_likes),
    path('authors/<str:author_id>/liked',views.get_author_liked),
    path('viewpost/',views.view_post),
]
