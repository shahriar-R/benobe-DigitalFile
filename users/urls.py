from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from . import views

app_name = "users"


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='auth_register'),
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
# router = DefaultRouter()
# router.register("rgister", views.RegisterView, basename="register")


# urlpatterns = router.urls
