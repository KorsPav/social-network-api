from django.urls import path
from .views import PostViewSet, PostLike


post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('', post_list, name='posts_list'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('<slug:slug>/like/', PostLike.as_view(), name='post-like'),  # [PUT] to like, [DELETE] to unlike
]
