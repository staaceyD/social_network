from rest_framework import generics
from .serializers import PostSerializer, PostLikeSerializer, PostDislikeSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated


class PostCreateApi(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostReadApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostUpdateApi(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDeleteApi(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDetailApi(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class LikeApiView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated]


class DislikeApiView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDislikeSerializer
    permission_classes = [IsAuthenticated]
