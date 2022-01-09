from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class CRSFExemptMisin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, **kwargs):
        return super().dispatch(request, **kwargs)
