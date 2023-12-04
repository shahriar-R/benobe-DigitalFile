from django.shortcuts import render
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import Http404 
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Patient
from .serializers import PatientSerializer


class PatientModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "firstname": [ "startswith"],
        "lastname": ["exact"],
        "phone": ["exact"],
    }

    # search_fields = ["title", "context"]
    # ordering_fields = ["create_date"]
    # pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
