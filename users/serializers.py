from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email(value):
	if 'admin' in value:
		raise serializers.ValidationError('admin cant be in email')


class UserRegisterSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = User
		fields = ('username', 'phone_number', 'password', 'password2')
		

	def create(self, validated_data):
		del validated_data['password2']
		return User.objects.create_user(**validated_data)

	def validate_username(self, value):
		if value == 'admin':
			raise serializers.ValidationError('username cant be `admin`')
		return value

	def validate(self, data):
		if data['password'] != data['password2']:
			raise serializers.ValidationError('passwords must match')
		return data
	

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'