from django.urls import include, path
from rest_framework.authtoken import views

app_name = 'users'


urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', views.obtain_auth_token),
]
