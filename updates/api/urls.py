from django.urls import path, re_path

from .views import UpdateModelDetailsApi, UpdateModelListApi

urlpatterns = [
    # path('cbv1/', JsonCBV1.as_view()),
    path('', UpdateModelListApi.as_view()),
    re_path('^(?P<id>\d+)/$', UpdateModelDetailsApi.as_view()),
    # path('cbv2/', JsonCBV2.as_view()),
    # path('updates/', update_model_detail_view, name='updates')
]
