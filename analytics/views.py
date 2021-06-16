from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from post.models import Like
from post.serializers import LikeSerializer


class LikesAnalyticsView(ListAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer

    def get(self, request, *args, **kwargs):
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')

        likes = Like.objects.filter(date__range=[date_from, date_to])

        result = dict()

        for i in likes:
            date_key = i.date.isoformat()
            if date_key in result:
                result[date_key] += 1
            else:
                result[date_key] = 1

        return Response(status=status.HTTP_200_OK, data={f'{result}'})
