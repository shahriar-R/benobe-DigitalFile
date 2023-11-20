from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin




class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BUM):
	def create_user(self, phone_number, username, password):
		if not phone_number:
			raise ValueError('user must have phone number')

		if not username:
			raise ValueError('user must have full name')

		user = self.model(phone_number=phone_number,  username=username)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, phone_number,username, password):
		user = self.create_user(phone_number, username, password)
		user.is_admin = True
		user.is_superuser = True
		user.save(using=self._db)
		return user
	

class User(BaseModel, AbstractBaseUser, PermissionsMixin):
	phone_number = models.CharField(max_length=11, unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	is_active = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'phone_number'
	REQUIRED_FIELDS = ['email', 'first_name','last_name']

	def __str__(self):
		return f"{self.first_name}_{self.last_name}"

	@property
	def is_staff(self):
		return self.is_admin