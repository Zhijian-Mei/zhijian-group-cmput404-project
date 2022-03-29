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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="Team 12 API",
      default_version='v1',
      description="Team 12",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('service/', include('socialdistribution.urls')),
    path('',views.index),
    path('',include("django.contrib.auth.urls")),
    path('myprofile/',views.my_profile),
    path('mypost/',views.my_post),
    path('mypost/create/',views.create_post, name='createpost'),
    path('mypost/edit/<str:id>',views.edit_post),
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
    path('myrequest/unfriend', views.unfriend, name='unfriend'),
    path('mysubscriptions/', views.my_subscriptions),
    path('friendonly/', views.friend_only),
    path('inbox/', views.like_and_share),
    path('foreign_posts/',views.get_foreign_posts)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
