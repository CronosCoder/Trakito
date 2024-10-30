from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/auth/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/v1/", include("todo.urls"))
]
