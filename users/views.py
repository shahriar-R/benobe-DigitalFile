from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer, CustomAuthTokenSerializer, ProfileSerializer
from .models import Profile

# Create your views here.
User = get_user_model()

# class RegistrationModelViewSet(viewsets.ViewSet):
#     serializer_class = RegistrationSerializer
    
#     def create(self, request, *args, **kwargs):
        
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data["username"]
#             password = serializer.validated_data["password1"]
#             user = User.objects.create_user(
#                 username=username, password=password
#             )
#             authenticate(request, username=username, password=password)
#             login(request, user)
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            phone_number = serializer.validated_data["phone_number"]
            data = {"phone_number": phone_number}
            user_obj = get_object_or_404(User, phone_number=phone_number)
            token = self.get_tokens_for_user(user_obj)
            return Response(data, status=status.HTTP_201_CREATED)
        return self.create(request, *args, **kwargs)
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
	
class CustomObtainAuthToken(ObtainAuthToken):

    serializer_class = CustomAuthTokenSerializer
	
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
		
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "phone_number": user.phone_number})

class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
	
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
