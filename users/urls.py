from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


app_name = 'accounts'
# urlpatterns = [
# 	path('register/', views.UserRegister.as_view()),
# 	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
# 	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

# router = routers.SimpleRouter()
# router.register('user', views.UserViewSet)
# urlpatterns += router.urls
    

urlpatterns = [
        
        path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
        path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),
    # login jwt
        path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt-create",
    ),
        path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
        path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),

]