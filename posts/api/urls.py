from django.conf.urls import url
from django.urls import path, include, re_path

from posts.api.views import PostApiView, PostCreateApiView, PostDetailsApiView, PostUpdateApiView, PostDeleteApiView

urlpatterns = [
    path('', PostApiView.as_view()),
    path('create', PostCreateApiView.as_view()),
    re_path('^(?P<id>\d+)/$', PostDetailsApiView.as_view()),
    re_path('(?P<id>.*)/update/$', PostUpdateApiView.as_view()),
    re_path('(?P<id>.*)/delete/$', PostDeleteApiView.as_view()),
]
