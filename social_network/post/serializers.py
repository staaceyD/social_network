from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["likes"]

    def update(self, instance, validated_data):
        instance.likes = instance.likes + 1
        instance.save()

        instance = super(PostLikeSerializer, self).update(instance, validated_data)

        return instance


class PostDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["likes"]

    def update(self, instance, validated_data):
        instance.likes = instance.likes - 1
        instance.save()

        instance = super(PostLikeSerializer, self).update(instance, validated_data)

        return instance
