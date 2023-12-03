from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "doctor"

router = DefaultRouter()
router.register("doctor", views.DoctorModelViewSet, basename="doctor")


urlpatterns = router.urls