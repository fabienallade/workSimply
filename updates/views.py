import json
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import View

from workSimply.mixins import JsonResponseMixin
from .models import Update


# Create your views here.
# def details_view(request):
#     return HttpResponse(get_template().render())

def update_model_detail_view(request):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    # return JsonResponse(json_data)
    return HttpResponse(json_data, content_type="application/json")


class JsonCBV1(View):
    def get(self, request, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)


class SerializeDetailView(JsonResponseMixin, View):
    def get(self, request, **kwargs):
        data = Update.objects.get(id=1).serialize()
        return HttpResponse(data, content_type="application/json")


class SerializeListView(JsonResponseMixin, View):
    def get(self, request, **kwargs):
        data = Update.objects.all().serialize()
        # data_json = serialize("json", data, fields=('user', 'content'))
        return HttpResponse(data, content_type="application/json")
