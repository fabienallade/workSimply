from django.urls import path, include, re_path

from categories.api.views import CategoryApiView, CategoryCreateApiView, CategoryDetailsApiView, CategoryUpdateApiView, \
    CategoryDeleteApiView

urlpatterns = [
    path('', CategoryApiView.as_view()),
    path('create', CategoryCreateApiView.as_view()),
    re_path('^(?P<id>.*)/$', CategoryDetailsApiView.as_view()),
    re_path('(?P<id>.*)/update/$', CategoryUpdateApiView.as_view()),
    re_path('(?P<id>.*)/delete/$', CategoryDeleteApiView.as_view()),
]
