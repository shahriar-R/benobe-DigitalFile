from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . models import Doctor, Secretary
from .serializers import DoctorSerializer, SecretarySerializer
from .permissions import IsDoctorPermission



class DoctorModelViewSet(viewsets.ModelViewSet):
    '''if admin set activate then is active (-)'''

    permission_classes = [IsAuthenticated, IsDoctorPermission]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    def create(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class SecretaryModelViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated, IsDoctorPermission]
    serializer_class = SecretarySerializer
    queryset = Secretary.objects.all()

    def create(self, request, *args, **kwargs):
        ''' if user is doctor can create (-)'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


