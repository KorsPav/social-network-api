from django.shortcuts import get_object_or_404
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
    queryset = Post.objects.order_by('-creation_date')
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLike(UpdateAPIView, DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def put(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        user = get_object_or_404(get_user_model(), username=request.user)
        try:
            Like.objects.get(user=user, post=post)
        except Like.DoesNotExist:
            Like.objects.create(user=user, post=post)
            return Response(status=status.HTTP_201_CREATED,
                            data={'Message': 'Liked'})
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={'Message': 'Already liked'})

    def delete(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        user = get_object_or_404(get_user_model(), username=request.user)
        try:
            obj = Like.objects.get(user=user, post=post)
            obj.delete()
        except Like.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'Message': 'Post not liked'})
        return Response(status=status.HTTP_200_OK,
                        data={'Message': 'Unliked'})
