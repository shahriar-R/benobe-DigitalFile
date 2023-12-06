from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver




class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BUM):
	def create_user(self, phone_number, password, **extra_fields):
		if not phone_number:
			raise ValueError('user must have phone number')

	
		user = self.model(phone_number=phone_number, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, phone_number, password,**extra_fields):
		user = self.create_user(phone_number, password, **extra_fields)
		user.is_admin = True
		user.is_superuser = True
		user.save(using=self._db)
		return user
	

class User(BaseModel, AbstractBaseUser, PermissionsMixin):
	phone_number = models.CharField(max_length=11, unique=True)
	
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'phone_number'
	

	def __str__(self):
		return self.phone_number

	@property
	def is_staff(self):
		return self.is_admin
	




class Profile(models.Model):
    """
    Profile class for each user which is being created to hold the information
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.phone_number


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """
    Signal for post creating a user which activates when a user being created ONLY
    """
    if created:
        Profile.objects.create(user=instance)