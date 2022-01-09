from django.urls import path, include, re_path

from products.api.views import ProductApiView, ProductCreateApiView, ProductDetailsApiView, ProductUpdateApiView, \
    ProductDeleteApiView

urlpatterns = [
    path('', ProductApiView.as_view()),
    path('create', ProductCreateApiView.as_view()),
    re_path('(?P<id>.*)/$', ProductDetailsApiView.as_view()),
    re_path('(?P<id>.*)/update/$', ProductUpdateApiView.as_view()),
    re_path('(?P<id>.*)/delete/$', ProductDeleteApiView.as_view()),
]
