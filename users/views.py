from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import UserRegisterSerializer, UserSerializer

# Create your views here.
User = get_user_model()

class UserRegister(APIView):
	def post(self, request):
		ser_data = UserRegisterSerializer(data=request.POST)
		if ser_data.is_valid():
			ser_data.create(ser_data.validated_data)
			return Response(ser_data.data, status=status.HTTP_201_CREATED)
		return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
	permission_classes = [IsAuthenticated,]
	queryset = User.objects.all()

	def list(self, request):
		srz_data = UserSerializer(instance=self.queryset, many=True)
		return Response(data=srz_data.data)

	def retrieve(self, request, pk=None):
		user = get_object_or_404(self.queryset, pk=pk)
		srz_data = UserSerializer(instance=user)
		return Response(data=srz_data.data)

	def partial_update(self, request, pk=None):
		user = get_object_or_404(self.queryset, pk=pk)
		if user != request.user:
			return Response({'permission denied': 'you are not the owner'})
		srz_data = UserSerializer(instance=user, data=request.POST, partial=True)
		if srz_data.is_valid():
			srz_data.save()
			return Response(data=srz_data.data)
		return Response(data=srz_data.errors)

	def destroy(self, request, pk=None):
		user = get_object_or_404(self.queryset, pk=pk)
		if user != request.user:
			return Response({'permission denied': 'you are not the owner'})
		user.is_active = False
		user.save()
		return Response({'message':'user deactivated'})
	
class CustomObtainAuthToken(ObtainAuthToken):
	pass
    # serializer_class = CustomAuthTokenSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(
    #         data=request.data, context={"request": request}
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data["user"]
    #     token, created = Token.objects.get_or_create(user=user)
    #     return Response({"token": token.key, "user_id": user.pk, "email": user.email})

class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)