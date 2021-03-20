from rest_framework import generics
from .serializers import PostSerializer, PostLikeSerializer, PostDislikeSerializer
from .models import Post


class PostCreateApi(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostReadApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateApi(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteApi(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailApi(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeApiView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer


class DislikeApiView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDislikeSerializer
