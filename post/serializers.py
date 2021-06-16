from rest_framework import serializers

from post.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'creation_date',
            'author',
            'likes',
            'slug',
        )


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = (
            'user',
            'post',
            'date',
        )
