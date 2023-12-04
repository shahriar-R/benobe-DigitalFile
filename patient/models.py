from django.db import models
from django.contrib.auth import get_user_model
import uuid

from doctor.models import Doctor


User = get_user_model()

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.id, filename)



class Patient(models.Model):

    gender_choices =  ( ('woman', "زن"),('men', "مرد"),)
        
    marital_choices =(("married", "متاهل"),("single", "مجرد"),)
    number_id = models.IntegerField(unique=True)
    date = models.CharField(max_length=30)
    files = models.FileField(upload_to=user_directory_path)
    
    date = models.CharField(max_length=30)
    type_test = models.TextField()
    out_test = models.TextField()
    date_test = models.DateTimeField()
    normal_values= models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    # file = models.ForeignKey(File, on_delete= models.SET_NULL,null=True, related_name="file")
    # test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True, related_name="test")
    national_code = models.CharField(max_length=10, unique=True,default=uuid.uuid1, null=True, blank=True)

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    born = models.IntegerField()# change
    age = models.IntegerField()
    phone = models.CharField(max_length=12,default="",unique=True)
    marital_status = models.CharField(choices=marital_choices,max_length=30)
    gender = models.CharField(choices=gender_choices, max_length=30)

    
    
    def __str__(self):
        return f"{self.firstname}-{self.lastname}"
