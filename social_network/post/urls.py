from django.urls import path
from .views import (
    PostCreateApi,
    PostReadApi,
    PostUpdateApi,
    PostDeleteApi,
    PostDetailApi,
    LikeApiView,
    DislikeApiView,
)


urlpatterns = [
    path("create", PostCreateApi.as_view(), name="create"),
    path("read", PostReadApi.as_view(), name="read"),
    path("update/<pk>", PostUpdateApi.as_view(), name="update"),
    path("delete/<pk>", PostDeleteApi.as_view(), name="delete"),
    path("details/<pk>", PostDetailApi.as_view(), name="detail"),
    path("like/<pk>", LikeApiView.as_view(), name="like"),
    path("dislike/<pk>", DislikeApiView.as_view(), name="like"),
]
