from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication

from .serializers import ProductSerializer
from ..models import Product


class ProductApiView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    authentification_classes = [SessionAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, **kwargs):
        return self.create(request, **kwargs)


class ProductCreateApiView(generics.CreateAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductDetailsApiView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)


class ProductUpdateApiView(generics.UpdateAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ProductDeleteApiView(generics.DestroyAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
