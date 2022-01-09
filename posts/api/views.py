from rest_framework import generics, mixins,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from posts.models import Post
from .serializers import PostSerializer


class PostApiView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentification_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, **kwargs):
        return self.create(request, **kwargs)



class PostCreateApiView(generics.CreateAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailsApiView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)


class PostUpdateApiView(generics.UpdateAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostDeleteApiView(generics.DestroyAPIView):
    permission_classes = []
    authentification_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
