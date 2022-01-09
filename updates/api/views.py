from django.http import HttpResponse
from django.views.generic import View
from .mixins import CRSFExemptMisin
from updates.forms import UpdateModelForm
from django.http import QueryDict
from .utils import is_json
import json

from updates.models import Update as UpdateModel


class UpdateModelDetailsApi(CRSFExemptMisin, View):

    def render_to_json(self, data, status=400):
        return HttpResponse(data, content_type="application/json", status=status)

    def get_object(self, id=None):
        try:
            obj = UpdateModel.objects.get(id=id)
        except UpdateModel.DoesNotExist:
            obj = None
        # qs = UpdateModel.objects.filter()
        # if qs.count() == 1:
        #     return qs.fist()
        return obj

    def get(self, request, id, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Data no found"})
            return self.render_to_json(error_data, status=401)
        # json_data = obj.serialize()
        data = obj.serialize()
        return HttpResponse(data, content_type="application/json")

    def put(self, request, id, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Data no found"})
            return self.render_to_json(error_data, status=401)
        # json_data = obj.serialize()
        if not is_json(request.body):
            error_data = json.dumps({"messages": "Veuillez renvoyer une donne json"})
            return self.render_to_json(error_data)

        passed_data = json.loads(request.body)
        form = UpdateModelForm(passed_data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_json(obj_data, status=200)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_json(data, status=400)

        # return self.render_to_json(data, status=401)

    def delete(self, request, id, **kwargs):
        if not is_json(request.body):
            error_data = json.dumps({"messages": "Veuillez renvoyer une donne json"})
            return self.render_to_json(error_data)
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Data no found"})
            return self.render_to_json(error_data, status=401)
        # json_data = obj.serialize()
        data, data_deleted = obj.delete()
        if data == 1:
            data_json = json.dumps({"messages": "deleted success"})
            return self.render_to_json(data_json, status=200)
        else:
            data_json = json.dumps({"messages": "Somethings went wrong"})
            return self.render_to_json(data_json, status=200)


class UpdateModelListApi(CRSFExemptMisin, View):

    def render_to_json(self, data, status=400):
        return HttpResponse(data, content_type="application/json", status=status)

    def get(self, request, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, **kwargs):
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_json(obj_data, status=200)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_json(data, status=400)
        json_data = json.dumps({"message": "Unknown data"})
        return self.render_to_json(json_data, status=200)

    def put(self, request, **kwargs):
        return  # json

    def delete(self, request, **kwargs):
        return  # json
