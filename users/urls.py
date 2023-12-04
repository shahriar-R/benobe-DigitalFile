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
        path('jwt/', include(([
            path('login/', TokenObtainPairView.as_view(),name="login"),
            path('refresh/', TokenRefreshView.as_view(),name="refresh"),
            path('verify/', TokenVerifyView.as_view(),name="verify"),
            ], "jwt")),),
        path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
        path(
            "token/logout/",
            views.CustomDiscardAuthToken.as_view(),
            name="token-logout",
        ),
]