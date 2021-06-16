from django.urls import path, include

from .views import signup, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


user_list = UserViewSet.as_view({
    'get': 'list',
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('', user_list, name='users_list'),
    path('<username>/', user_detail, name='user_detail'),
    path('auth/', include('rest_framework.urls')),  # login and logout
    path('auth/signup/', signup, name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
