from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet
from rest_framework.authtoken import views

app_name = 'users'

router = DefaultRouter()

router.register('users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', views.obtain_auth_token),
]
