from django.urls import path 
from rest_framework.routers import DefaultRouter

from . import views

app_name = "patient"

router = DefaultRouter()
router.register("patient", views.PatientModelViewSet, basename="patient")
router.register("test", views.TestModelViewSet, basename="test")
router.register("file", views.FileModelViewSet, basename="file")

urlpatterns = router.urls

# urlpatterns = [ 
    
#     path('patient/<int:pk>/', views.PatientDetail.as_view()), 
# ] 