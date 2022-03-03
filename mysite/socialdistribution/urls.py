from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/',views.post_list),
    path('createpost/',views.create_post,name='api_createpost'),
    path('authors/',views.get_authors),
    path('authors/<str:author_id>',views.get_author),
    path('viewpost/',views.view_post),
    path('authors/<str:author_id>/posts/<str:post_id>',views.get_post)
]

