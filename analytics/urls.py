from django.urls import path
from .views import LikesAnalyticsView


urlpatterns = [
    path('', LikesAnalyticsView.as_view(), name='likes_analytics'),
]
