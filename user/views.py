from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import SNUser
from .serializers import UserSerializer, UserCreateSerializer
from .permissions import IsAdminOrOwnerOrReadOnly


class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminOrOwnerOrReadOnly)
    queryset = SNUser.objects.order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'username'


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def signup(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)
