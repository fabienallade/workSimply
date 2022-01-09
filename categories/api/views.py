from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from categories.api.serializers import CategorySerializer
from categories.models import Category


class CategoryApiView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentification_classes = [SessionAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        qs = Category.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, **kwargs):
        return self.create(request, **kwargs)


class CategoryCreateApiView(generics.CreateAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailsApiView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)


class CategoryUpdateApiView(generics.UpdateAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class CategoryDeleteApiView(generics.DestroyAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
