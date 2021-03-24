from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["like"]

    def update(self, instance, validated_data):
        instance.like = instance.like + 1
        instance.save()

        instance = super(PostLikeSerializer, self).update(
            instance, validated_data)

        return instance


class PostDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["like"]

    def update(self, instance, validated_data):
        instance.like = instance.like - 1
        instance.save()

        instance = super(PostDislikeSerializer, self).update(
            instance, validated_data)

        return instance
